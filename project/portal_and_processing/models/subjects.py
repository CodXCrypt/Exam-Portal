from django.db import models

from .enums import Levels, Schools


class Subject(models.Model):
    Name = models.CharField(
        max_length=72, unique=True, null=False, default="Undefined Subject"
    )
    Level = models.CharField(max_length=12, choices=Levels.choices(), blank=False)
    School = models.CharField(max_length=31, choices=Schools.choices(), blank=False)
