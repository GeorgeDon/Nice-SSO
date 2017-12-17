import redis
from sso import ssoCache
from django.http import HttpResponse
from models import t_user
import json
import uuid

def login(request):
    # # ssoCache.set("lei","su")
    # test=ssoCache.get("lei")
    # response = HttpResponse(test)
    # return response
    if request.method == 'POST':
        received_json_data = json.loads(request.body, encoding='utf-8')
        print received_json_data
        userName = received_json_data.get("name")
        pwd = received_json_data.get("pwd")
        userNum = t_user.objects.filter(userName=userName).count()
        if userNum == 0:
            response = HttpResponse("ERROR")
            return response
        user = t_user.objects.get(userName=userName)
        if user.pwd == pwd:
            token = uuid.uuid4().hex
            ssoCache.set(userName,token)
            tokenjson = {}
            tokenjson['token'] = token

            response = HttpResponse(json.dumps(tokenjson), content_type="application/json")
            return response
        response = HttpResponse("user or password is error!")
        return response
    response = HttpResponse("ERROR")
    return response
