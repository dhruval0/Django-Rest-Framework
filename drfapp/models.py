from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    user_name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_name