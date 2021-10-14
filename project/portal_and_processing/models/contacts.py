import uuid

from django.db import models

from .students import Student


class Contact(models.Model):
    """
    Fill in the models as per DB Schema
    """
    uuid = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    Name = models.OneToOneField(
        Student, related_name='contact', on_delete=models.CASCADE
    )
    Contact_Number = models.BigIntegerField()
    Email = models.EmailField()
