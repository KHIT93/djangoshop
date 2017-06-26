from django.shortcuts import render
from products.models.product import Product
# Create your views here.

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

	#def get_context_data(self, *args, **kwargs):
	#	context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
	#	context["title"] = "This is about us"
	#	return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["product_list"] = Product.objects.all()[:12]
        return self.render_to_response(context)
