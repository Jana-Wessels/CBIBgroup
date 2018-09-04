from django.conf.urls import url
from papers import views

urlpatterns = [
    url(r'^publications/$', views.search_form, name='publications'),
    url('upload/', views.paper_form, name='paperupload'),
    url(r'^search/$', views.search),
    #url(r'^publications/$', views.getAuthor),
]