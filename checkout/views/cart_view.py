from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.

from django.views.generic.base import TemplateView
from checkout.models.cart import Cart
from checkout.models.cart_item import CartItem
from products.models.product import Product
from customers.models.customer import Customer

class CartView(TemplateView):
    template_name = "cart.html"

    def get_object(self, *args, **kwargs):
        self.request.session.set_expiry(0) #5 minutes
        cart_id = self.request.session.get("cart_id")
        if cart_id == None:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
        if self.request.user.is_authenticated():
            customer, created = Customer.objects.get_or_create(user=self.request.user)
            cart.customer = customer
            cart.save()
        return cart

    def get_context_data(self, *args, **kwargs):
        context = super(CartView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()
        return context

    def get(self, request, *args, **kwargs):
        return super(CartView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        cart = self.get_object()
        item_id = request.POST.get("item")
        delete_item = request.POST.get("delete", False)
        item_added = False
        if item_id:
            item_instance = get_object_or_404(Product, id=item_id)
            qty = request.POST.get("qty", 1)
            try:
                if int(qty) < 1:
                    delete_item = True
            except:
                raise Http404
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=item_instance)
            if created:
                item_added = True
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
            return self.get(request, *args, **kwargs)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
