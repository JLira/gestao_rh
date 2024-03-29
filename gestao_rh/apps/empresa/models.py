import uuid
from django.db import models

class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    name = models.CharField(max_length=100, help_text='Nome da Empresa')

    def __str__(self):
        return f'{self.name}'