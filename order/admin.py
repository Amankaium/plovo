from django.contrib import admin
from .models import Order, Restaurant

class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'dish', 'location', 'status')
    list_editable = ("status",)
    search_fields = ('dish__name', 'location')
    list_filter = ('status',)

admin.site.register(Order, OrderAdmin)
admin.site.register(Restaurant)
