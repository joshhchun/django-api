import uuid
from django.db import models

# Create your models here.

class TimeStampedUUIDModel(models.Model):
    # Pseudo-primary key
    pkid=models.BigAutoField(primary_key = True, editable = False)
    id=models.UUIDField(default = uuid.uuid4, unique = True, editable = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]