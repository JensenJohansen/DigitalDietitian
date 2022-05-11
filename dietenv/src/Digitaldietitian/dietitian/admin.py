from django.contrib import admin
# from django.contrib.auth.models import User
from .models import User
from Customer.models import *

admin.site.register(User)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email',)
admin.site.register(Zone)


