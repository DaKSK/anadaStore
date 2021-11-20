from products.models import Product, Category


class ProductForm:
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm:
    class Meta:
        model = Category
        fields = '__all__'
