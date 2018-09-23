from django.contrib import admin
from django.conf.urls import url
from . import views	


urlpatterns = [
    url('', views.all_blogs, name='allblogs'),
    url('<int:blog_id>/', views.detail, name='detail' ),
] 		