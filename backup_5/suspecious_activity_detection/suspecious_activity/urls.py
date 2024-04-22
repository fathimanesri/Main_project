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
    path('editpolis/<int:id>',views.editpolis,name="editpolis"),
    path('edit_post',views.edit_post,name="edit_post"),
    path('managecriminallist',views.managecriminallist,name="managecriminallist"),
    path('editcriminal/<int:id>', views.editcriminal, name="editcriminal"),
    path('managepolice',views.managepolice,name="managepolice"),
    path('sentreport/<int:id>',views.sentreport,name="sentreport"),
    path('reply_post',views.reply_post,name="reply_post"),
    path('stationhome', views.stationhome, name="stationhome"),
    path('taskstatus', views.taskstatus, name="taskstatus"),
    path('assigntasktopolice', views.assigntasktopolice, name="assigntasktopolice"),
    path('viewcomplaint', views.viewcomplaint, name="viewcomplaint"),
    path('viewreport', views.viewreport, name="viewreport"),
    path('police_code', views.police_code, name="police_code"),
    path('police', views.police, name="police"),
    path('criminal', views.criminal, name="criminal"),
    path('deletecriminal/<int:id>', views.deletecriminal, name="deletecriminal"),
    path('deletpolicestation/<int:id>', views.deletpolicestation, name="deletpolicestation"),
    path('deletpolice/<int:id>', views.deletpolice, name="deletpolice"),
    path('editstation/<int:id>', views.editstation, name="editstation"),
    path('editcriminals', views.editcriminals, name="editcriminals"),
    path('assigntask', views.assigntask, name="assigntask"),
    path('police_station', views.police_station, name="police_station"),


]
