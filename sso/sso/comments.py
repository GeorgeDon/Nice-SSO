# coding= utf-8
import json
from django.http import HttpResponse
from models import t_comment
from django.forms.models import model_to_dict

def comment(request):
    com = t_comment.objects.all().values('message', 'date').order_by('-id')[:10]
    comList = list(com)
    count = t_comment.objects.all().count()
    datajson = {}
    datajson['Total'] = count
    datajson['comments'] = comList
    return HttpResponse(json.dumps(datajson), content_type="application/json")
