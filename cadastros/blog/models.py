from django.db import models
from django.conf import settings

# Create your models here.
class Usuario(models.Model):

    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"],
    

    ]
    codigo = models.IntegerField(null=True)
    endereco = models.CharField(max_length=200, null = True)
    numero = models.IntegerField(null=True)
    cidade = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=2, null=True)
    datanasc = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    cpf = models.IntegerField(null=True)
    rg = models.IntegerField(null=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=1, choices= SEXO_CHOICES)

