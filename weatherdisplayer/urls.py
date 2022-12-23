
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]