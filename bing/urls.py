from . import views
from django.conf.urls import url

#app_name = 'bing'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
]