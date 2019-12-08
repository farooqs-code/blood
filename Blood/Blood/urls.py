"""Blood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from SaveTheSoul import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',TemplateView.as_view(template_name='main.html')),

    path('home/',views.home.as_view(),name='home'),
    path('adm/',views.ad.as_view(),name='ad'),
    path('dnr/',views.donor.as_view(),name='donor'),
    path('org/',views.orgs.as_view(),name='orgs'),
    path('visit/',views.visit.as_view(),name='visit'),
    path('login/',views.login,name='login'),



]
