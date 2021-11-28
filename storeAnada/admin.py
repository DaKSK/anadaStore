from django.contrib import admin

from products.models import Category, Product, Purchase, Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price', 'slug', 'created', 'updated']
	list_filter = ['is_active']
	list_editable = ['price']
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
	list_display = ['user', 'product', 'quantity', 'date']
	list_filter = ['date', 'updated']


admin.site.register(Profile)
