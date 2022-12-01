from unicodedata import name
from django.db import models

# Create your models here.

class Data(models.Model):
    image_id = models.IntegerField(db_column='imageid')
    name = models.CharField(max_length=45)
    #description = models.TextField(blank=True, null=True)
    birthday = models.CharField(max_length=45, default = True)
    sex = models.CharField(max_length=45, default = True)
    temperature = models.FloatField(default = True)
    weight = models.FloatField(default = True)
    height = models.FloatField(default = True)
    pressures = models.IntegerField(db_column='pressureS')
    pressured = models.IntegerField(db_column='pressureD')
    #updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name