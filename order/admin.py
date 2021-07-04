from django.contrib import admin


from .models import Order, AdditionDish, Restaurant

class AdditionDishInline(admin.TabularInline):
    model = AdditionDish
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'dish', 'location', 'status')
    list_editable = ("status",)
    search_fields = ('dish__name', 'location')
    list_filter = ('status',)
    inlines = [AdditionDishInline]

admin.site.register(Order, OrderAdmin, Restaurant)


class AdditionDishAdmin(admin.ModelAdmin):
    list_display = ('dish', 'order', 'created_at', 'updated_at')
    fields = ('dish', 'order', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(AdditionDish, AdditionDishAdmin)
 
