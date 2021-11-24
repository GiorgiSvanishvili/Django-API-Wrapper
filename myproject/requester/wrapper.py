import requests
from .models import Info


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


if __name__ == '__main__':
    requester()
