from django.db import models
from apps.funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, models.PROTECT)

    def __str__(self):
        return self.descricao
