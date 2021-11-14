from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView
from products.models import Product, Category


class ProductCreateView(CreateView):
    # template_name = "product_create.html"
    # form_class = ProductCreateForm
    # success_url = reverse_lazy("success")
    pass


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
