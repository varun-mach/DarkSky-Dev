from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login,{'template_name' : 'demosky/login.html'}),
	url(r'^logout/$', logout,{'template_name' : 'demosky/logout.html'}),
	url(r'^register/$', views.register),
	url(r'^profile/$', views.profile),
]