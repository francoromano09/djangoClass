from django.db import models

class Products(models.Model): #Hereda de models
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=50, unique=True)