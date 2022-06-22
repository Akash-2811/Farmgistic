from django.db import models

# Create your models here.
class crop_details(models.Model):
    crop_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/index/')
    
    def __str(self):
        return self.crop_name