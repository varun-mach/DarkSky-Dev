from django.db import models
from django.contrib.auth.models import User

class EmailUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.IntegerField()
    



# Create your models here.
