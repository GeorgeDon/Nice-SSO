# coding= utf-8
import json
from django.http import HttpResponse
from models import t_user
from common import log

@log("excute")
def addUser(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body,encoding='utf-8')
        userName = received_json_data.get("name")
        userAlias = received_json_data.get("alias")
        pwd = received_json_data.get("pwd")
        oldUser = t_user.objects.filter(userName=userName).count()
        if oldUser == 1:
            response = HttpResponse("user" + userName)
            return response
        newUser = t_user(userName=userName, userAlias=userAlias, pwd=pwd)
        newUser.save()
        response = HttpResponse("ok")
        return response
    response = HttpResponse("ERROR")
    return response
