from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import CharField

# Create your models here.

# Construção do modelo Funcionário e seus atributos.
class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    celular = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    
    rg = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    salario = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    # As operações de busca no modelo são definidas através de um Manager.
    objetos = models.Manager()

    # A criação das tabelas no banco de dados deve ser feita com os comandos makemigrations e migrate.
