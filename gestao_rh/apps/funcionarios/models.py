import uuid
from django.db import models

class Funcionarios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text='Nome do funcionário')

    def __str__(self):
        return f'{self.name}'  