import uuid
from django.db import models

class Documento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=100, help_text='Nome do documento')
    
    def __str__(self):
        return f'{self.descricao}'