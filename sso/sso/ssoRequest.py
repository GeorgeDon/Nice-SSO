# coding= utf-8
import json
from django.http import HttpResponse
from models import t_user
from common import log
from django.shortcuts import render_to_response

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

@log("excute")
def listUser(request):
    if request.method == 'GET':
        # page = int(request.GET.get('page'))
        # size = int(request.GET.get('size'))
        # index_from = (page - 1) * size
        # index_to = index_from + size
        # user = t_user.objects.all().values('userName', 'userAlias', 'userType').order_by('-id')[index_from:index_to]
        user = t_user.objects.all().values('userName', 'userAlias', 'userType').order_by('-id')
        count = t_user.objects.all().count()
        userList = list(user)
        # try:
        datajson = {}
        datajson['users'] = userList
        datajson['count'] = count
        # return HttpResponse(json.dumps(datajson), content_type="application/json")
        return render_to_response('sso/uses.html', datajson)
