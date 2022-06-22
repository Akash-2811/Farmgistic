from django.db import models
from authentication.models import farmer_auth, trader_auth

# Create your models here.
class crops(models.Model):
    farmer_id = models.ForeignKey(farmer_auth, on_delete=models.CASCADE, to_field="id", db_column="farmer_id")
    crop_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image_link = models.CharField(max_length=255, blank=True)
    
    
    def __str(self):
        return self.crop_name


class images(models.Model):
    crop_id = models.ForeignKey(crops, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)

    def __str(self):
        return self.link


class request(models.Model):
    crop_id = models.ForeignKey(crops, on_delete=models.CASCADE)
    trader_id = models.ForeignKey(trader_auth, on_delete=models.CASCADE)
    is_confirm = models.BooleanField(max_length=255)

    def __str(self):
        return self.link