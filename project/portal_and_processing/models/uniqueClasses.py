from django.db import models
from .teachers import teachers

class UniqueClasses(models.Model):
    Strength = models.IntegerField()
    Teacher = models.ForeignKey(teachers)