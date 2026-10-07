"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from alpha.views import article, home, landing, search

urlpatterns = [
    path('', home, name='home'),
    path('app/', home, name='home_app'),
    path('app/article/<int:pk>/', article, name='article'),
    path('article/<int:pk>/', article),
    path('app/search/', search, name='search'),
    path('search/', search),
    path('landing/', landing, name='landing'),
    path('admin/', admin.site.urls),
]
