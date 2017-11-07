from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.getlist, name='getlist'),
    url(r'^getfilename',views.getfilename, name='getfilename'),
    url(r'^goaction',views.goaction, name='goaction'),

]
