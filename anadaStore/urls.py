"""anadaStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import storeAnada.views

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # HOME
    path('', TemplateView.as_view(template_name='store/home.html'), name='home'),
    # PRODUCTS
    path('products/create', storeAnada.views.ProductCreateView.as_view(), name='product-create'),
    path('products/success', TemplateView.as_view(template_name='store/success.html'), name='success'),
    path('products/', storeAnada.views.ProductListView.as_view(), name='product-list'),
    path('products/<pk>', storeAnada.views.ProductDetailView.as_view(), name='product-detail'),
    path('products/update/<pk>', storeAnada.views.ProductUpdateView.as_view(), name='products-update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
