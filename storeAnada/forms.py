from products.models import Product, Category
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SignUpForm(UserCreationForm):
    password2 = None

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1']
