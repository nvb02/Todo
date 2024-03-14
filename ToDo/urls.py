"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path #we use path function to create urls that takes 2 arguments -- 1. string(that is written on the web browser),  2. what request should be passed or called
from base.views import home, create #importing create function that is rendering create.html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('create/', create,name='home') #every path is a url.. 2 arguments is necessary inside the path --> 1. url name, 2. function or view to be called through url (the function must include request and response which is render that displays create.html))
]
