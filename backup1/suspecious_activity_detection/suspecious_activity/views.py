from django.shortcuts import render

# Create your views here.



def login(request):
    return render(request,"login.html")


def addpolicestation(request):
    return render(request,"admin/add police station.html")

def admin(request):
    return render(request,"admin/admin.html")

def feedback(request):
    return render(request,"admin/feedback.html")

def managepolicestation(request):
    return render(request,"admin/manage police station.html")

def viewcrimerecord(request):
    return render(request,"admin/v crime record.html")
def viewcriminalist(request):
    return render(request,"admin/vi criminal list.html")


def addcriminallist(request):
    return render(request,"police station/add crim list.html")

def addpolis(request):
    return render(request,"police station/add police.html")

def managecriminallist(request):
    return render(request,"police station/manage criminallist.html")

def managepolice(request):
    return render(request,"police station/manage police.html")


def sentreport(request):
    return render(request,"police station/sent report.html")

def stationhome(request):
    return render(request,"police station/station home.html")

def taskstatus(request):
    return render(request,"police station/task status.html")

def assigntasktopolice(request):
    return render(request,"police station/tast to police.html")

def viewcomplaint(request):
    return render(request,"police station/V compliant.html")

def viewreport(request):
    return render(request,"police station/vi report.html")