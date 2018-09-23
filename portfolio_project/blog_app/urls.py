from django.contrib import admin
from django.conf.urls import url
from blog_app import views	


urlpatterns = [
    url('', views.all_blogs, name='allblogs'),
] 