from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('mp3.views',

   url(r'^$', 'view_index', name='casa'),
) 
