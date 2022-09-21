from django.contrib import admin
from .models import Shopcart
from .models import Payment

# Register your models here.
@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['user','dish', 'c_name', 'quantity','c_item', 'c_date', 'c_price', 'amount']
    list_editable = ['c_name', 'quantity','c_price','amount']
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','phone','total', 'cart_code', 'pay_code', 'pay_date', 'paid', 'admin_note', 'admin_update']
    readonly_fields = ['user','first_name', 'last_name','phone','total', 'cart_code', 'pay_code', 'pay_date', 'paid',]
