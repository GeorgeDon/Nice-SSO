from sso import ssoCache

def checkLogin(user, token):
    rtoken = ssoCache.get(user)
    if rtoken and rtoken == token:
        return True
    else:
        return False





