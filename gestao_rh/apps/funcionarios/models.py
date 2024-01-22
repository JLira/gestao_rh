import uuid
from django.db import models
from django.contrib.auth.models import User

from gestao_rh.apps.departamentos.models import Departamento
from gestao_rh.apps.empresa.models import Empresa


class Funcionarios(models.Model):
    class Meta:
        db_table = 'rh_funcionario'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, help_text='Nome do funcionário')
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
