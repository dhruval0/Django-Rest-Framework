from statistics import mode
from telnetlib import Telnet
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    date_created = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title