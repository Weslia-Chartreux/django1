from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'price']
    search_fields = ['name', ]
    empty_value_display = '-Нема-'


admin.site.register(models.Product, ProductAdmin)
