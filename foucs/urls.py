from django.conf.urls import url
from .views import index
from . import views
urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^log_out/$', views.log_out, name='log_out'),
	url(r'^log_up/$', views.log_up, name='log_up'),
	url(r'^artical/(?P<artical_id>[0-9]+)/$', views.artical_detail, name='artical_detail'),
]