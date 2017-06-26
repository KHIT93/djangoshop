from django.views.generic import DetailView
from ..models import Product


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['product_price'] = 100
        #context['product_name'] = "Hej"

        return context