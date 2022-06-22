from django.db import models
from datetime import datetime

# Create your models here.

class farmer_auth(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
     

    def __str(self):
        return self.first_name


class trader_auth(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    photo = models.ImageField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name