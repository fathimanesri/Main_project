from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from suspecious_activity.models import *


def login(request):
    return render(request,"login.html")

def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=username,password=password)
        if ob.type=='admin' :
            return HttpResponse('''<script>alert("success");window.location="/admin"</script>''')

        elif ob.type == 'station':
            return HttpResponse('''<script>alert("success");window.location="/stationhome"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username");window.location="/"</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert("invalid username");window.location="/"</script>''')




def addpolicestation(request):
    return render(request,"admin/add police station.html")

def admin(request):
    return render(request,"admin/admin.html")

def feedback(request):
    ob=feedback_table.objects.all()
    return render(request,"admin/feedback.html",{'val':ob})

def managepolicestation(request):
    ob=policestation_table.objects.all()
    return render(request,"admin/manage police station.html",{'val':ob})

def viewcrimerecord(request):
    return render(request,"admin/v crime record.html")


def viewcriminalist(request):
    ob=criminal_table.objects.all()
    return render(request,"admin/vi criminal list.html",{'val':ob})


def addcriminallist(request):
    ob=criminal_table.objects.all()
    return render(request,"police station/add crim list.html",{'val':ob})

def addpolis(request):
    return render(request,"police station/add police.html")

def managecriminallist(request):
    ob = criminal_table.objects.all()
    return render(request,"police station/manage criminallist.html",{'val':ob})

def managepolice(request):
    ob=police_table.objects.all()
    return render(request,"police station/manage police.html",{'val':ob})


def sentreport(request):
    return render(request,"police station/sent report.html")

def stationhome(request):
    return render(request,"police station/station home.html")

def taskstatus(request):
    ob=police_table.objects.all()
    return render(request,"police station/task status.html",{'val':ob})

def assigntasktopolice(request):
    return render(request,"police station/tast to police.html")

def viewcomplaint(request):
    ob = complaint_table.objects.all()
    return render(request,"police station/V compliant.html",{'value':ob})

def viewreport(request):
    ob = report_table.objects.all()
    return render(request,"police station/vi report.html",{'value':ob})