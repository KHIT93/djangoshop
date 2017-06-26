from django.views.generic import TemplateView
from customers.models.customer import Customer


class MyAccountDetailView(TemplateView):
    template_name = "myaccount_detail.html"
    model = Customer
    context_object_name = "customer"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MyAccountDetailView, self).get_context_data(**kwargs)

        return context