"""projectRoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('article_page/', views.article_page, name="article_page"),
    path('top_picks/', views.top_picks, name="top_picks"),
    path('product_page/<name>', views.product_page, name="product_page"),
    path('filter_page/', views.filter_page, name="filter_page"),
    path('library_page/', views.library_page, name="library_page"),
    path('add_beer/', views.form_view, name="add_beer"),
    path('contact/', views.contact_page, name="contact"),
    path('about/', views.about_page, name="about"),
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup_page, name="signup"),
]
