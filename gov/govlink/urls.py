from django.urls import path
from .views import CourseList, CourseCategory
from . import views 
from .views import Home
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'govlink'
urlpatterns = [
     path('', Home.as_view(), name ='Home'),
     url(r'^category/$', views.CourseCategory.as_view(), name ='CourseCategory'),
     url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_add'),
     url(r'^post/add/$', views.PostCreate.as_view(), name='post_add'),
     
     path('/courselist/<int:pk>', views.CourseList.as_view(), name = 'courselist'),
     #path('post/add/', views.Post_create, name='PostCreate'),
    ]
