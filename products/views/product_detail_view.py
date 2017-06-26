from django.views.generic import DetailView
from ..models import Product


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        return context