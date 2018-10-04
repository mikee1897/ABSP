from django.urls import path
from django.conf.urls import include, url
from .import views
from django.views.generic import TemplateView

app_name='main'
urlpatterns = [
  
    path('home/', views.home, name='home'),
    path('personal_info/', views.personal_info, name='personal_info'),
    path('question1/', views.question1, name='question1'),
    path('question2/', views.question2, name='question2'),
    path('end_page/', views.end_page, name='end_page'),   
];