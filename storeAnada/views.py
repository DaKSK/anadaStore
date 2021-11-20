from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
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
