from products.models.category import Category
from products.models.product import Product
from django.views.generic import ListView


class ProductListView(ListView):
    template_name = "product_list.html"
    model = Product
    context_object_name = "product"

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Store the categories in the context
        context["category_list"] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = Product.objects.all()

        # Filter on category if there is one selected
        if 'pk' in self.kwargs:
            queryset = queryset.filter(category=self.kwargs['pk'])

        # Filter on search string if one is part of the get
        if self.request.GET.get('search'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('search'))
        return queryset

