from django.views.generic import ListView
from products.models.category import Category
from products.models.product import Product


class ProductListView(ListView):
    template_name = "product_list.html"
    model = Category
    context_object_name = "category"

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)

        if 'pk' in self.kwargs:
            context['product_list'] = Product.objects.filter(category=self.kwargs['pk'])
        else:
            context['product_list'] = Product.objects.all()[:12]

        query = self.request.GET.get('search')
        if query:
            context['product_list'] = Product.objects.filter(name__icontains=query)

        return context
