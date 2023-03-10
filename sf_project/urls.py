"""sf_project URL Configuration

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

admin.site.site_header = "Привет с города Николаева!"
admin.site.site_title = "Админка"
admin.site.index_title = ": D"



urlpatterns = [
    path('', admin.site.urls),
    path('greeting  ', include('django.contrib.flatpages.urls')),
    path('1/', include('django.contrib.flatpages.urls')),
    path('2/', include('django.contrib.flatpages.urls')),
    path('default/', include('django.contrib.flatpages.urls')),

]
