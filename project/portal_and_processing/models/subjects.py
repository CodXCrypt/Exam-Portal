from django.db import models
from .enums import levels, schools


class Subjects(models.Model):
    Name = models.CharField(
        max_length=72, unique=True, null=False, default="Undefined Subject"
    )
    Level = models.CharField(max_length=72, choices=levels, blank=False)
    School = models.CharField(max_length=72, choices=schools, blank=False)
