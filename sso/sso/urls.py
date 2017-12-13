"""sso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ssoRequest import addUser
from ssoValid import login
from ssoEml import sml
from comments import comment
from leaveMessage import leave_message

urlpatterns = [
    url(r'^sso/v1/users/',addUser),
    url(r'^sso/v1/login/', login),
    url(r'^sso/v1/sendEmail/', sml),
    url(r'^v1/comments/', comment),
    url(r'^v1/leaveMessage/', leave_message),
]
