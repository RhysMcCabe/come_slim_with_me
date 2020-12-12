from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['billingName', 'created', 'emailAddress', 'status',]

admin.site.register(Order, OrderAdmin)
