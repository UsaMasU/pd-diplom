from django.contrib import admin
from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'user', 'state')
    list_filter = ('name', 'user')
    search_fields = ('name', 'user')
    #prepopulated_fields = {'slug': ('name',)}
    #ordering = ('name', 'id')
