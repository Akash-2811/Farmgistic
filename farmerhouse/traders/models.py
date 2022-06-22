from django.db import models
from authentication.models import farmer_auth
from farmers.models import crops
from datetime import datetime

# Create your models here.
class orders(models.Model):
    crops_id = models.ForeignKey(crops, on_delete=models.CASCADE, null=True)
    trader_id = models.IntegerField(null=True)
    created_date = models.DateField(default=datetime.now)