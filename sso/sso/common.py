# coding= utf-8
from sso import ssoCache
import functools
import ssoLog
from django.http import HttpResponse
import json

def checkLogin(user, token):
    rtoken = ssoCache.get(user)
    if rtoken and rtoken == token:
        return True
    else:
        return False
# def deco(func):
#     def _deco(*args, **kwargs):
#         print "before %s called." % func.__name__
#         ret = func(*args, **kwargs)
#         print "after %s called. result: %s" % (func.__name__, ret)
#         return ret
#     return _deco
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            ssoLog.logger.info('%s %s():' % (text, func.__name__))
            try:
                return func(*args, **kw)
            except Exception, ex:
                error = Exception, ':', ex
                ssoLog.logger.error(error)
                responseData = {}
                responseData['status'] = 500
                response = HttpResponse(json.dumps(responseData), content_type="application/json")
                return response
        return wrapper
    return decorator


