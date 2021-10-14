from django.contrib.auth.models import User
from django.db import models

from .subjects import Subject


class Student(models.Model):
    User = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    Name = models.CharField(max_length=108, unique=False, blank=False)
    Class = models.PositiveSmallIntegerField(unique=False, blank=False)
    Section = models.CharField(max_length=1, unique=False, blank=False)
    UniqueClassID = models.ForeignKey(
        "UniqueClasses", related_name='students', on_delete=models.DO_NOTHING
    )
    Subject_One = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_one"
    )
    Subject_Two = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_two"
    )
    Subject_Three = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_three"
    )
    Subject_Four = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_Four"
    )
    Subject_Five = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_five"
    )
