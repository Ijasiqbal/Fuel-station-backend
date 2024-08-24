from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reading(models.Model):
    name = models.CharField(max_length=100,null=True)
    dispensingUnit = models.IntegerField(null=True)
    nozzle1and2 = models.BooleanField(null=True)
    nozzle3and4 = models.BooleanField(null=True)
    nozzle3and4 = models.BooleanField(null=True)
    openingNozzle1 = models.FloatField(null=True)
    openingNozzle2 = models.FloatField(null=True)
    openingNozzle3 = models.FloatField(null=True)
    openingNozzle4 = models.FloatField(null=True)
    closingNozzle1 = models.FloatField(null=True)
    closingNozzle2 = models.FloatField(null=True)
    closingNozzle3 = models.FloatField(null=True)
    closingNozzle4 = models.FloatField(null=True)
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