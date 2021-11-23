from django.db import models
import requests

# Create your models here.


class Info(models.Model):
    login = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)


def requester():
    data = Info.objects.all()
    if Info.id == '43324003' in data:
        return data
    else:
        response = requests.get("https://api.github.com/users/Luff3x").json()
        login = response.get('login')
        id = response.get('id')
        name = response.get('name')
        user = Info.objects.create(login=login, id=id, name=name)
        user.save(force_insert=True)
