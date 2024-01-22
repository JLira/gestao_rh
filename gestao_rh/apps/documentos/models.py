import uuid
from django.db import models

from gestao_rh.apps.funcionarios.models import Funcionarios


class Documento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=100, help_text='Nome do documento')
    owner = models.ForeignKey(Funcionarios, on_delete=models.PROTECT )

    def __str__(self):
        return f'{self.descricao}'
