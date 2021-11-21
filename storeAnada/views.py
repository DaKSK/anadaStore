from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView
from products.models import Product, Category
from products.forms import ProductForm


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product


class ProductCreateView(CreateView):
    template_name = "products/product_create.html"
    form_class = ProductForm
    success_url = reverse_lazy('success')


class ProductUpdateView(UpdateView):
    template_name = "products/product_create.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('success')


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    model = Product


# View for passing Product model to home.html, to show the product images and names in grid
class HomeView(TemplateView):
    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()[:3]
        return context


class PurchaseView():
    pass

