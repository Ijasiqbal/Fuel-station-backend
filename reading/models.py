from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reading(models.Model):
    name = models.CharField(max_length=100,null=True)
    dispensingUnit = models.IntegerField(null=True)
    nossle = models.IntegerField(null=True)
    openingP = models.FloatField(null=True)
    openingD = models.FloatField(null=True)
    closingP = models.FloatField(null=True)
    closingD = models.FloatField(null=True)
    cash = models.FloatField(null=True)
    card = models.FloatField(null=True)
    paytm = models.FloatField(null=True)
    oil = models.FloatField(null=True)
    credit = models.FloatField(null=True)
    expected = models.FloatField(null=True)
    received = models.FloatField(null=True)
    shortage = models.FloatField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


    def __str__(self):
        return self.name    