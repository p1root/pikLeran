from django.contrib import admin
from .models import Discount
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass