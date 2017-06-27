from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from checkout.models.cart import Cart
from checkout.models.cart_item import CartItem
from app_settings.models.app_setting import AppSetting
from orders.models.order import Order
from orders.models.order_line import OrderLine
#from djangoshop.mixins.login_required_mixin import LoginRequiredMixin
import json
import stripe

class CheckoutConfirmationView(TemplateView):
    template_name = "checkout_confirm.html"

    def get_cart(self, *args, **kwargs):
        self.request.session.set_expiry(0) #5 minutes
        cart_id = self.request.session.get("cart_id")
        if cart_id == None:
            raise Http404
        cart = Cart.objects.get(id=cart_id)
        return cart

    def get_context_data(self, *args, **kwargs):
        context = super(CheckoutConfirmationView, self).get_context_data(*args, **kwargs)
        context["cart"] = self.get_cart()
        try:
            context["stripe_key"] = AppSetting.objects.get(key="STRIPE_PUBLISHABLE_KEY")
        except AppSetting.DoesNotExist:
            context["stripe_key"] = None
        return context

    def get(self, request, *args, **kwargs):
        if self.get_context_data(*args, **kwargs)["cart"].cartitem_set.count == 0:
            return HttpResponseRedirect(reverse("cart"))
        return super(CheckoutConfirmationView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = None
        token = None
        cart = self.get_cart()
        payment_method = None
        if request.is_ajax():
            data = json.loads(request.body)
            token = data["stripeToken"]
            payment_method = data["payment_method"]
        else:
            data = request.POST
            payment_method = request.POST.get("payment_method")
        invoiced = False
        if payment_method == "stripe":
            stripe.api_key = AppSetting.objects.get(key="STRIPE_SECRET_KEY").value
            charge = stripe.Charge.create(
                amount=cart.total_in_lowest(),
                currency="usd",
                description="Payment for order",
                source=token,
            )
            invoiced = True

        context = super(CheckoutConfirmationView, self).get_context_data(*args, **kwargs)
        order = Order.objects.create(customer=cart.customer, invoiced=invoiced)
        for i in cart.cartitem_set.all():
            OrderLine.objects.create(order=order, product=i.product, quantity=i.quantity)

        order.update_total()
        cart.delete()
        del self.request.session["cart_id"]
        self.request.session["order_id"] = order.id
        self.request.session.modified = True

        if request.is_ajax():
            data = {
                "status": "OK",
                "url": reverse("checkout_complete")
            }
            return JsonResponse(data)

        return HttpResponseRedirect(reverse("checkout_complete"))
