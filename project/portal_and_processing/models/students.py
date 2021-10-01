from django.db import models
from django.contrib.auth.models import User

from .subjects import Subjects


class Student(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=108, unique=False, blank=False, null=False)
    UniqueID = models.UUIDField()
    Class = models.IntegerField()
    Section = models.CharField(max_length=1, unique=False, blank=False)
    Subject_One = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, related_name="Subject One+"
    )
    Subject_Two = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, related_name="Subject Two+"
    )
    Subject_Three = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, related_name="Subject Three+"
    )
    Subject_Four = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, related_name="Subject Four+"
    )
    Subject_Five = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, related_name="Subject Five+"
    )
