from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "sketchfab"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'sketchfab/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'sketchfab/logout.html'}, name='logout')
]
