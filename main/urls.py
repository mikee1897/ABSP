from django.urls import path
from django.conf.urls import include, url
from .import views
from django.views.generic import TemplateView

app_name='main'
urlpatterns = [

    path('index/', views.index, name='index'),
    path('', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    # path('choose_language/', views.choose_language, name='choose_language'),
    # path('first_language/', views.first_language, name='first_language'),
    # path('second_language/', views.second_language, name='second_language'),
    path('page3/', views.page3, name='page3'),
    #path('page4/', views.page4, name='page4'),
    path('page4/', views.page5, name='page5'),
    path('page5/', views.page6, name='page6'),
    path('page6/', views.page7, name='page7'),
    #path('page8/', views.page8, name='page8'),
    #path('page9/', views.page9, name='page9'),
    path('page7/', views.page10, name='page10'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('invest/', views.invest, name='invest'),
    path('table-data/', views.table_data, name='table_data'),
    path('page8/', views.page11, name='page11'),
    path('page9/', views.page12, name='page12'),
    path('page10/', views.page13, name='page13'),   
    path('participants/', views.participants, name='participants'),   
];