import uuid

from django.db import models
from django.contrib.auth.models import User

from .enums import Levels
from .subjects import Subject
from .contacts import Contact


class Teacher(models.Model):
    User = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, blank=False)
    UniqueID = models.UUIDField(unique=True, default=uuid.uuid4)
    Subject = models.ForeignKey(Subject, related_name="teachers", on_delete=models.DO_NOTHING)
    Level = models.CharField(max_length=12, choices=Levels.choices())
    Contact = models.OneToOneField(
        Contact, to_field="uuid", related_name="teacher", on_delete=models.CASCADE
    )
    Last_Logged_in = models.DateTimeField(auto_now_add=True)
    Date_of_registration = models.DateField(auto_created=True)
    Access_Class = models.ForeignKey(
        "UniqueClasses", related_name="teachers", on_delete=models.CASCADE
    )

    