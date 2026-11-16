from django.db import models


# Create your models here.
class Mensaje(models.Model):
    texto = models.TextField()
