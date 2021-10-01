from django.db import models
from django.contrib.auth.models import User

from .enums import levels
from .subjects import Subjects
from .contacts import contacts
from .uniqueClasses import UniqueClasses

class teachers(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    Name = models.CharField(max_length = 100, null = False, blank = False)
    UniqueID = models.UUIDField()
    Subject = models.ForeignKey(Subjects, on_delete = models.DO_NOTHING)
    Level = models.CharField(max_length = 100, choices = levels)
    Contact = models.ForeignKey(contacts, on_delete = models.CASCADE)
    Last_Logged_in = models.DateTimeField(auto_now_add = True)
    Date_of_registration = models.DateField(auto_created=True)
    Access_Class = models.ForeignKey(UniqueClasses, on_delete = models.CASCADE)

    