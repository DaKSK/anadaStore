from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView, FormView
from products.models import Product, Category, Purchase
from products.forms import ProductForm, PurchaseForm


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


class PurchaseView(FormView):
    template_name = "store/purchase.html"
    form_class = PurchaseForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        print("purchase done")
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(id=self.kwargs['pk'])[0]
        return context

    def get_initial(self):
        initial = super(PurchaseView, self).get_initial()
        product = Product.objects.get(id=self.kwargs['pk'])
        initial.update({'product': product.pk, 'user': self.request.user.pk})
        return initial

    # def get_form_kwargs(self):
    #     kwargs = super(PurchaseView, self).get_form_kwargs()
    #     product = Product.objects.filter(id=self.kwargs['pk'])[0]
    #     kwargs['product'] = product.pk
    #     kwargs['user'] = self.request.user.pk
    #
    #     return kwargs

