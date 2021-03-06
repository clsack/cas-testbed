"""casclient2 URL Configuration

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
from django.urls import path
import django_cas_ng.views

from casclient2.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login', django_cas_ng.views.login, name='cas_ng_login'),
    path('accounts/logout', django_cas_ng.views.logout, name='cas_ng_logout'),
    path('accounts/callback', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
    path('', index, name='index'),
]
