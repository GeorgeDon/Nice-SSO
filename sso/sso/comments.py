# coding= utf-8
import json
from django.http import HttpResponse
from models import t_comment

def comment(request):
    page =int( request.GET.get('page'))
    size = int(request.GET.get('size'))
    index_from=(page-1)*size
    index_to=index_from+size
    com = t_comment.objects.all().values('message', 'date').order_by('-id')[index_from:index_to]
    count = t_comment.objects.all().count()
    comList=list(com)
    # try:
    datajson = {}
    datajson['comments'] = comList
    datajson['count'] = count
    return HttpResponse(json.dumps(datajson), content_type="application/json")
    # except
