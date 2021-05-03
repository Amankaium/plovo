from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'dish', 'location', 'status')
    list_editable = ("status",)
    search_fields = ('dish__name', 'locations')
    list_filter = ('status',)

admin.site.register(Order, OrderAdmin)
