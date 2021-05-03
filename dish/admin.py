from django.contrib import admin
from .models import Dish

# Register your models here.


class DishAdmin(admin.ModelAdmin):
    fields = ('name', 'price')
    readonly_fields = ['name']

admin.site.register(Dish, DishAdmin)