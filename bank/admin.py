from django.contrib import admin
from .models import customer,cust_phone,account,trans_info

# Register your models here.

admin.site.register(customer)
admin.site.register(cust_phone)
admin.site.register(account)
admin.site.register(trans_info)