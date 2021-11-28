# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView, FormView, DeleteView

from products.forms import ProductForm, PurchaseForm
from products.models import Product, Category


class ProductListView(ListView):
	template_name = "products/product_list.html"
	model = Product

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		search = self.request.GET.get('search', None)
		products = Product.objects.all()
		if search:
			products = products.filter(title__contains=search)  # Contains gives flexibility in the search input
			context['search'] = search
		context['products'] = products
		return context


class CategoryListView(ListView):
	template_name = "products/categories.html"
	# template_name = "products/product_list.html"
	model = Category

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	category = self.request.GET.get('category', None)
	# 	search = self.request.GET.get('search', None)
	# 	products = Product.objects.all()
	# 	if category:
	# 		products = products.filter(category__id=int(category))
	# 	context['products'] = products
	#
	# 	# SEARCH
	# 	return context

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# THIS CATEGORY -> the URL query string parameter
		category = self.request.GET.get('category', None)
		search = self.request.GET.get('search', None)
		products = Product.objects.all()
		if category:
			context['category'] = category
			products = products.filter(category__id=int(category))  # Filter by FieldNameinProductModel__FieldInFKModel
		if search:
			products = products.filter(title__contains=search)  # Contains gives flexibility in the search input
			context['search'] = search

		context['products'] = products

		return context


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


class ProductDeleteView(DeleteView):
	template_name = 'products/product_delete.html'
	model = Product
	success_url = reverse_lazy('product-list')
