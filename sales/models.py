from django.db import models

class Sales(models.Model):
    fuelSales = models.FloatField(null=True)
    debit = models.FloatField(null=True)
    oil = models.FloatField(null=True)
    itemSales = models.FloatField(null=True)
    openingBalance = models.FloatField(null=True)
    totalCash = models.FloatField(null=True)
    totalCard = models.FloatField(null=True)
    totalPaytm = models.FloatField(null=True)
    credit = models.FloatField(null=True)
    closingBalance = models.FloatField(null=True)
    shortage = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True) 
    time = models.TimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = ("Sales")
        verbose_name_plural = ("Saless")


class ClosingSales(models.Model):
    Du1Nozzle1 = models.FloatField(null=True)
    Du1Nozzle2 = models.FloatField(null=True)
    Du1Nozzle3 = models.FloatField(null=True)
    Du1Nozzle4 = models.FloatField(null=True)
    Du2Nozzle1 = models.FloatField(null=True)
    Du2Nozzle2 = models.FloatField(null=True)
    Du2Nozzle3 = models.FloatField(null=True)
    Du2Nozzle4 = models.FloatField(null=True)
    Du3Nozzle1 = models.FloatField(null=True)
    Du3Nozzle2 = models.FloatField(null=True)
    Du3Nozzle3 = models.FloatField(null=True)
    Du3Nozzle4 = models.FloatField(null=True)
    Du4Nozzle1 = models.FloatField(null=True)
    Du4Nozzle2 = models.FloatField(null=True)
    Du4Nozzle3 = models.FloatField(null=True)
    Du4Nozzle4 = models.FloatField(null=True)

    class Meta:
        verbose_name = ("ClosingSales")
        verbose_name_plural = ("ClosingSaless")