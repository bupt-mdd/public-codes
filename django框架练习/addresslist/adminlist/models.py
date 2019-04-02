from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user=models.ForeignKey(User)
    newname=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    QQ_number=models.CharField(max_length=30)
    address=models.CharField(max_length=30)