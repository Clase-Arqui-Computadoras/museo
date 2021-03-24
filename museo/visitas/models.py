from django.db import models

# Create your models here.
class Visita(models.Model):
    email = models.EmailField()
    timestamp_in = models.DateTimeField()
    timestamp_out = models.DateTimeField()
    comment = models.CharField(max_length=140)