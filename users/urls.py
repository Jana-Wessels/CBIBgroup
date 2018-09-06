from django.conf.urls import url
from . import views
from users import views

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url('user/', views.user_detail, name='user_detail'),
    url('edit/', views.user_edit, name='user_edit'),

]