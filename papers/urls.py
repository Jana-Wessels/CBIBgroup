from django.conf.urls import url
from papers import views

urlpatterns = [
    url(r'^publications/$', views.search_form, name='publications'),
    url(r'^paper/(?P<pk>[0-9]+)/$', views.paper_detail, name='paper_detail'),
    url(r'paper/(?P<pk>[0-9]+)/edit/', views.paper_edit, name='paper_edit'),
    url('upload/', views.paper_form, name='paperupload'),
    url(r'^search/$', views.search),
]