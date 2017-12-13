# coding= utf-8
import json
from django.http import HttpResponse
from models import t_comment
import time


def leave_message(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body, encoding='utf-8')
        message = received_json_data.get("message")
        date=time.strftime('%Y-%m-%d', time.localtime(time.time()))
        newMessage = t_comment(message=message,date=date)
        newMessage.save()
        response = HttpResponse("ok")
        return response
    response = HttpResponse("ERROR")
    return response
