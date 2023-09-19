from django.db import models

class CreditTransaction(models.Model):
    name = models.CharField(max_length=255, null=True)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    debit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    transaction_date = models.DateField(null=True)
    transaction_time = models.TimeField(null=True)

    def __str__(self):
        return self.name
