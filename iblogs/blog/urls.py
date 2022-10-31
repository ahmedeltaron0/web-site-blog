"""iblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import *

urlpatterns = [
   path('welcome/', views.welcome, name="welcome"),
   path('register/', views.registerPage, name="register"),
   path('login/', views.loginPage, name="login"),
   path('logout/', views.logoutUser, name="logout"),
   path('home/',home ,name="home"),
   path('blog/<slug:url>', post),
   path('category/<slug:url>', category),
   path('post/<int:pk>/comment/',AddCommentView.as_view() , name="add_comment"),
   path('blogpost-like/<slug:url>', views.BlogPostLike, name="blogpost_like"),
   path('add_post/',AddPostView.as_view(),name='add_post'),
   path('add_category/',AddCategoryView.as_view(),name='add_Category'),


]
