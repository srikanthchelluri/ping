from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^login/$', views.login_auth, name='login'),
	url(r'^signup/$', views.signup_auth, name='signup'),
	url(r'^logout/$', views.logout_auth, name='logout'),

	url(r'^home/$', views.home, name='home'),
	url(r'^send_ping/$', views.send_ping, name='send_ping'),	
]