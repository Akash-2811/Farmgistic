from django.contrib import admin
from .models import farmer_auth, trader_auth

# Register your models here.
admin.site.register(farmer_auth)
admin.site.register(trader_auth)