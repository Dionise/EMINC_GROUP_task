from django.db import models

# Create your models here.


class Data_CSV(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(default=None, blank=True)
    
    def __str__(self):
         return self.name


class Data_JSON(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(default=None, blank=True)

    
    def __str__(self):
         return self.name