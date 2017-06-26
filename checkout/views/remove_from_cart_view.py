from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from checkout.models.cart import Cart
from checkout.models.cart_item import CartItem
from products.models.product import Product

class RemoveFromCartView(View):
    #template_name = "cart.html"

    def get_object(self, *args, **kwargs):
        self.request.session.set_expiry(0) #5 minutes
        cart_id = self.request.session.get("cart_id")
        if cart_id == None:
            cart = Cart()
            cart.tax_percentage = 0.25
            cart.save()
            cart_id = cart.id
            self.request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
        if self.request.user.is_authenticated():
            cart.user = self.request.user
            cart.save()
        return cart

    def post(self, request, *args, **kwargs):
        cart = self.get_object()
        item_id = request.POST.get("item")
        delete_item = request.POST.get("delete", False)
        if item_id:
            item_instance = get_object_or_404(Variation, id=item_id)
            qty = request.POST.get("qty", 1)
            try:
                if int(qty) < 1:
                    delete_item = True
            except:
                raise Http404
            if delete_item:
                cart_item.delete()
            if not request.is_ajax():
                return HttpResponseRedirect(reverse("cart"))
                #return cart_item.cart.get_absolute_url()
        return HttpResponseRedirect(reverse("cart"))
