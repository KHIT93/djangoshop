from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from orders.models.order import Order

class CheckoutCompletedView(TemplateView):
    template_name = "checkout_complete.html"

    def get_order(self, *args, **kwargs):
        self.request.session.set_expiry(0) #5 minutes
        order_id = self.request.session.get("order_id")
        if order_id == None:
            raise Http404
        order = Order.objects.get(id=cart_id)
        return order

    def get_context_data(self, *args, **kwargs):
        context = super(CheckoutCompletedView, self).get_context_data(*args, **kwargs)
        context["order"] = self.get_order()
        return context

    def get(self, request, *args, **kwargs):
        if self.request.session.get("order_id") == None:
            return HttpResponseRedirect(reverse("cart"))
        #del self.request.session["order_id"]
        #self.request.session.modified = True
        return super(CheckoutCompletedView, self).get(request, *args, **kwargs)
