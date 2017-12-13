# coding= utf-8
import json
from django.http import HttpResponse
from models import t_comment
from django.forms.models import model_to_dict

def comment(request):
    com = t_comment.objects.all().values('message', 'date').order_by('-id')[:10]
    print 1
    comList=list(com)
    print 2
    count = t_comment.objects.all().count()
    datajson = {}
    datajson['Total'] = count
    datajson['comments'] = comList
    print datajson
    return HttpResponse(json.dumps(datajson), content_type="application/json")
