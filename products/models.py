from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)  

    def __str__(self):
        return self.name