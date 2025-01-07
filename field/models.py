from django.db import models
from django.conf import from django.conf import settings

class Field(models.Model):

    farmer_id = models.IntegerField()
    name = models.CharField(max_length = 100)
    size_in_hectars = models.DecimalField( max_digits=5, decimal_places=2)
    location = models.CharField(max_length=255)
    crop_type = models.CharField( max_length=100)

    def __str__(self):
        return f'{self.name} ({self.size_in_hectars} га - {self.crop_type})'
        
# Create your models here.
