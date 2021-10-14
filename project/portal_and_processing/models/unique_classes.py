from django.db import models
from .teachers import Teacher


class UniqueClasses(models.Model):
    Strength = models.IntegerField()
    Teacher = models.ForeignKey(
        Teacher, related_name="classes", on_delete=models.DO_NOTHING
    )
