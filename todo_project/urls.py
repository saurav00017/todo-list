"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from auapp.views import login,logout,resetpassword,changepassword,signup,createtask,viewtask,delete
from todoapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name = 'login'),
    path('login/',login,name = 'login'),
    path('logout/',logout,name = 'logout'),
    path('resetpassword/',resetpassword,name = 'resetpassword'),
    path('changepassword/',changepassword,name = 'changepassword'),
    path('signup/',signup,name = 'signup'),
    path('viewtask/',viewtask,name = 'viewtask'),
    path('createtask/',createtask,name = 'createtask'),
    path('delete/<int:id>',delete,name = 'delete')   
]
