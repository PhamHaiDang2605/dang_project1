from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'address', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Thông tin bổ sung', {'fields': ('phone', 'address')}),
    )

admin.site.register(Customer, CustomerAdmin)
