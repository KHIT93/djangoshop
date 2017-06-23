from django.shortcuts import render

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
        return self.render_to_response(context)
