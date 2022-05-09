from django.contrib import admin
# from django.contrib.auth.models import User
from .models import User
from Customer.models import *

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Zone)
admin.site.register(Role)

