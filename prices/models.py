from django.db import models

class Price(models.Model):
    petrol = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Petrol Price')
    diesel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Diesel Price')
    extrapremium = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Extra Premium Price')
    extragreen = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Extra Green Price')

    def __str__(self):
        return f"Price - Petrol: {self.petrol}, Diesel: {self.diesel}, Extra Premium: {self.extrapremium}, Extra Green: {self.extragreen}"

    class Meta:
        verbose_name_plural = 'Prices'
        app_label = 'prices'
