from django.db import models
from .students import Student
from .teachers import teachers

class contacts(models.Model):
    ...
    """
    Fill in the models as per DB Schema
    """
    Name = models.ForeignKey(Student, on_delete = models.CASCADE)
    Contact_Number = models.BigIntegerField()
    Email = models.EmailField()
    Teacher_name = models.ForeignKey(teachers, on_delete=models.CASCADE)
