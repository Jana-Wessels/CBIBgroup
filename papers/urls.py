from django.conf.urls import url
from papers import views

urlpatterns = [
    url(r'^publications/$', views.search_form, name='publications'),
    url(r'^search/$', views.search),
    #url(r'^publications/$', views.getAuthor),
]