from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'dish', 'location', 'status')
    list_editable = ("status",)

admin.site.register(Order, OrderAdmin)
