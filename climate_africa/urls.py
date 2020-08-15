"""climate_africa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

urlpatterns = [
    path('', include('common.urls', 'common')),
    path('story/', include('story.urls', 'story')),
    path('browse/', include('browse.urls', 'browse')),
    path('compose/', include('compose.urls', 'compose')),
    path('map/', include('map.urls', 'map')),
    path('menu/', include('menu.urls', 'menu')),
    path('admin/', admin.site.urls),
]
