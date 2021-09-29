from django.db import models

# Create your models here.
class User(models.Model):

    password = models.CharField(max_length=12)
    bio = models.TextField()
    birthday = models.DateField(null=True)
