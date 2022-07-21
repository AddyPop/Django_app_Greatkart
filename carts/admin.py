from django.contrib import admin
from carts.models import Cart, CartItem
# Register your models here.

class cartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class cartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, cartAdmin)
admin.site.register(CartItem, cartItemAdmin)