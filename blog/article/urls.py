"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from article import views


app_name = 'article'
urlpatterns = [
    path('', views.article, name='article'),
     path('articleCreate/', views.articleCreate, name='articleCreate'),
     path('articleRead/<int:articleId>/', views.articleRead, name='articleRead'),
     path('articleUpdate/<int:articleId>/', views.articleUpdate, name='articleUpdate'),
     path('articleDelete/<int:articleId>/', views.articleDelete, name='articleDelete'),
     path('articleSearch/', views.articleSearch, name='articleSearch'),
]
