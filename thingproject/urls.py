"""thingproject URL Configuration

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
# from things.views import things_view, home_view
# from things import urls
# from things.views import things_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', things_view, name='things'),
    # path('', home_view, name='home'),
    # path('', things_view, name='things_view')
    path('', include('things.urls'))
]
