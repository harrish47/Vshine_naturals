from django.db import models

class Catagories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name
