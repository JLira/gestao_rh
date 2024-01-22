import uuid
from django.db import models


class Departamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text='Nome do departamento')

    def __str__(self):
        return f'{self.name}'
