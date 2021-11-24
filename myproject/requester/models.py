from django.db import models
# Create your models here.


class Info(models.Model):
    login = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
