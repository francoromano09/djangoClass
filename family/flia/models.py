from django.db import models

class Parient(models.Model):
    name = models.CharField(max_length=50)
    dni = models.IntegerField()
    live = models.BooleanField()
