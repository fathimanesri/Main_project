"""suspecious_activity_detection URL Configuration

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

from suspecious_activity import views

urlpatterns = [


    path('',views.login,name="login"),
    path('logincode',views.logincode,name="logincode"),
    path('addpolicestation',views.addpolicestation,name="addpolicestation"),
    path('admin', views.admin,name="admin"),
    path('feedback',views.feedback,name="feedback"),
    path('managepolicestation',views.managepolicestation, name="managepolicestation"),
    path('viewcrimerecord',views.viewcrimerecord,name="viewcrimerecord"),
    path('viewcriminalist',views.viewcriminalist,name="viewcriminalist"),
    path('addcriminallist',views.addcriminallist,name="addcriminallist"),
    path('addpolis',views.addpolis,name="addpolis"),
    path('managecriminallist',views.managecriminallist,name="managecriminallist"),
    path('managepolice',views.managepolice,name="managepolice"),
    path('sentreport',views.sentreport,name="sentreport"),
    path('stationhome', views.stationhome, name="stationhome"),
    path('taskstatus', views.taskstatus, name="taskstatus"),
    path('assigntasktopolice', views.assigntasktopolice, name="assigntasktopolice"),
    path('viewcomplaint', views.viewcomplaint, name="viewcomplaint"),
    path('viewreport', views.viewreport, name="viewreport"),


]
