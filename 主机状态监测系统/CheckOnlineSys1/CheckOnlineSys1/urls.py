"""CheckOnlineSys1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','CheckOnline.views.getLogin'),
    url(r'^register/$','CheckOnline.views.register'),
    url(r'^getLoginName/$',"CheckOnline.views.getLoginName"),
    url(r'^getIpAddressList/$', "CheckOnline.views.getIpAddressList"),
    url(r'^addIp/$', "CheckOnline.views.addIp"),
    url(r'^addNetSeg/$', "CheckOnline.views.addNetSeg"),
    url(r'^delIp/$', "CheckOnline.views.delIp"),
    url(r'^delNetSeg/$', "CheckOnline.views.delNetSeg"),
    url(r'^checkUI/$','CheckOnline.views.checkUI'),
    url(r'^adminUserUI/$','CheckOnline.views.adminUserUI'),
    url(r'^delUser/$','CheckOnline.views.delUser'),
    url(r'^getUserList/$','CheckOnline.views.getUserList'),
    url(r'^exit/$','CheckOnline.views.exit'),
    #url(r'^exitInfo/$','CheckOnline.views.exitInfo'),
    #url(r'^exitPassword/$','CheckOnline.views.exitPassword'),
]
