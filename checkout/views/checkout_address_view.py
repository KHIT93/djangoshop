from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from checkout.models.cart import Cart
from checkout.models.cart_item import CartItem
from customers.models.customer import Customer
from checkout.forms.checkout_address_form import CheckoutAddressForm
#from djangoshop.mixins.login_required_mixin import LoginRequiredMixin

class CheckoutAddressView(TemplateView):
    template_name = "checkout_address.html"

    def get_cart(self, *args, **kwargs):
        self.request.session.set_expiry(0) #5 minutes
        cart_id = self.request.session.get("cart_id")
        if cart_id == None:
            raise Http404
        cart = Cart.objects.get(id=cart_id)
        return cart

    def get_context_data(self, *args, **kwargs):
        context = super(CheckoutAddressView, self).get_context_data(*args, **kwargs)
        context["cart"] = self.get_cart()
        context["form"] = CheckoutAddressForm(instance=context["cart"].customer)
        return context

    def get(self, request, *args, **kwargs):
        if self.get_context_data(*args, **kwargs)["cart"].cartitem_set.count == 0:
            return HttpResponseRedirect(reverse("cart"))
        return super(CheckoutAddressView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=self.request.user)
        form = CheckoutAddressForm(request.POST, instance=customer)
        form.save()

        return HttpResponseRedirect(reverse("checkout_confirm"))
