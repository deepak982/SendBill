from django.contrib import admin
from .models import *

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email',)
admin.site.register(Purchase,PurchaseAdmin)