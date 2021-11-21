from django.forms import (
    ModelForm, Form, CharField, Textarea, DecimalField, ImageField, SlugField,
    BooleanField, DateTimeField, IntegerField, HiddenInput
)
from products.models import Product, Category, Purchase


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


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
        widgets = {
            'product': HiddenInput(),
            'user': HiddenInput()
        }

    # def __init__(self, *args, **kwargs):
    #     super(PurchaseForm, self).__init__(*args, **kwargs)
    #     self.initial['product'] = kwargs['product']
    #     self.initial['user'] = kwargs['user']

