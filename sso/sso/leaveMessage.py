# coding= utf-8
import json
from django.http import HttpResponse
from models import t_comment
import time
from common import checkLogin
from common import log

@log("excute")
def leave_message(request):
    responseData={}
    if request.method == 'POST':
        # header=json.loads(request.header)
        token = request.META.get('HTTP_TOKEN')
        user = request.META.get('HTTP_USERNAME')
        if token and user:
            if not checkLogin(user,token):
                responseData['status'] = 401
                response = HttpResponse(json.dumps(responseData), content_type="application/json")
                return response
            received_json_data = json.loads(request.body, encoding='utf-8')
            message = received_json_data.get("message")
            date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            newMessage = t_comment(message=message, date=date)
            newMessage.save()
            responseData['status'] = 200
            response = HttpResponse(json.dumps(responseData), content_type="application/json")
            return response
        responseData['status'] = 401
        response = HttpResponse(json.dumps(responseData), content_type="application/json")
        return response
    responseData['status']=504
    response = HttpResponse(json.dumps(responseData), content_type="application/json")
    return response
