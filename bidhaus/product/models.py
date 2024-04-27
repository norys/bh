from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, default="")
    description = models.CharField(max_length=2048, default="")
    price = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=False)
