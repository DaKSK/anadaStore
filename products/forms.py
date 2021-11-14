from django.forms import (
    ModelForm, Form, CharField, Textarea, DecimalField, ImageField, SlugField,
    BooleanField, DateTimeField
)
from products.models import Product, Category


class ProductForm(ModelForm):
    # title = CharField(max_length=200)
    # description = Textarea()
    # image = ImageField()
    # price = DecimalField()
    # # category =
    # slug = SlugField(max_length=200)
    # in_stock = BooleanField()
    # is_active = BooleanField()
    class Meta:
        model = Product
        fields = "__all__"

