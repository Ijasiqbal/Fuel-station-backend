from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reading(models.Model):
    name = models.CharField(max_length=100,null=True)
    dispensingUnit = models.IntegerField(null=True)
    nossle = models.IntegerField(null=True)
    openingP = models.IntegerField(null=True)
    openingD = models.IntegerField(null=True)
    closingP = models.IntegerField(null=True)
    closingD = models.IntegerField(null=True)
    cash = models.IntegerField(null=True)
    card = models.IntegerField(null=True)
    paytm = models.IntegerField(null=True)
    oil = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)
    expected = models.IntegerField(null=True)
    received = models.IntegerField(null=True)
    shortage = models.IntegerField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


    def __str__(self):
        return self.name    