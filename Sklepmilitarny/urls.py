"""Sklepmilitarny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Produkty.views import *
from django.conf import settings
from django.conf.urls.static import static
from Produkty import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexx, name='home'),
    path('kategoria/<id>/', views.kategoria, name='kategoria'),
    path('produkt/<id>/', views.produkt, name='produkt'),
    path('search', views.search, name='search'),
    path('galeria', views.galeria, name='galeria'),
    path('kontakt', views.kontakt, name='kontakt'),
   # path('produkty/', include('Produkty.urls')),
    path('pogoda', include('Produkty.urls')),
    path('signup', views.signup_page, name='signup_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
