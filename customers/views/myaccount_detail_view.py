
from django.shortcuts import render
from customers.models.customer import Customer
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView

from ..forms import CustomerForm


class MyAccountDetailView(TemplateView):
    template_name = "myaccount_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MyAccountDetailView, self).get_context_data(*args, **kwargs)
        context["customer"] = Customer.objects.get_or_create(user=self.request.user)
        context["form"] = CustomerForm(instance=self.request.user.customer)
        return context

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=self.request.user)
        form = CustomerForm(request.POST, instance=customer)
        form.save()

        return HttpResponseRedirect(reverse("myaccount"))

