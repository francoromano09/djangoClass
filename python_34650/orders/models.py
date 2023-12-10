from django.db import models

class Order(models.Model):
    CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        )

    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices = CHOICES,max_length=4)

