import uuid
from django.db import models

from gestao_rh.apps.funcionarios.models import Funcionarios


class RegistroHoraExtra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.motivo}'
