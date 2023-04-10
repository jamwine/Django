"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from jamwine_blog.views import page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_view, {'page': 'home'}, name='home'),
    path('about', page_view, {'page': 'about'}, name='about'),
    path('music', page_view, {'page': 'music'}, name='music'),
    path('tech', page_view, {'page': 'tech'}, name='tech'),
    path('investing', page_view, {'page': 'investing'}, name='investing'),
    path('gaming', page_view, {'page': 'gaming'}, name='gaming'),
    path('merchandise', page_view, {'page': 'merchandise'}, name='merchandise'),
    path('travel', page_view, {'page': 'travel'}, name='travel'),
    path('contact', page_view, {'page': 'contact'}, name='contact'),
    # path('epicyclic_data/', epicyclic_data, name='epicyclic_data'),
]
