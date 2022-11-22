from django.db import models

class TransactionTypes(models.TextChoices):
    INCOME = "Entrada",
    OUTCOME = "Saida",

class Transaction(models.Model):
    type = models.CharField(
        max_length=10, 
        choices=TransactionTypes.choices, 
        default=TransactionTypes.INCOME
    )
    description = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    business = models.ForeignKey("businesses.Business", on_delete=models.CASCADE, related_name="transactions")
