from django.db import models

# Create your models here.
class Equipaments(models.Model):
    name_equipment = models.CharField(max_length=100)
    tipo_equipment = models.CharField(max_length=100)
