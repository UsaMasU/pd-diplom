from django.contrib import admin
from .models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, \
    Contact, Order, OrderItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass
    #list_display = ('name', 'url', 'user', 'state')
    #list_filter = ('name', 'user')
    #search_fields = ('name', 'user')
    #prepopulated_fields = {'slug': ('name',)}
    #ordering = ('name', 'id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
