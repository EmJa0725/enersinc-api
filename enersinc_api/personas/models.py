from django.db import models

# Create your models here.

class Persona(models.Model):
    class Meta:
        db_table = "persona"

    tipo_documento = models.CharField(max_length=2)
    documento = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)  
    apellidos = models.CharField(max_length=100)  
    hobbie = models.TextField(max_length=500)