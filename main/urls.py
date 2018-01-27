from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^generate/$', views.generate, name='generate'),
]
