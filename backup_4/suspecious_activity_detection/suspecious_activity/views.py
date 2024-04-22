from django.core.files.storage import FileSystemStorage
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
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("success");window.location="/stationhome"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username");window.location="/"</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert("invalid username");window.location="/"</script>''')




def addpolicestation(request):
    return render(request,"admin/add police station.html")
def police_code(request):
    nm=request.POST['textfield']
    ph=request.POST['textfield2']
    pl=request.POST['textfield3']
    em=request.POST['textfield4']
    un=request.POST['textfield5']
    ps=request.POST['textfield6']

    ob=login_table()
    ob.username=un
    ob.password=ps
    ob.type="station"
    ob.save()
    oj=policestation_table()
    oj.login=ob
    oj.place=pl
    oj.Name=nm
    oj.phone=ph
    oj.email=em
    oj.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location="/managepolicestation"</script>''')


def admin(request):
    return render(request,"admin/admin.html")

def feedback(request):
    ob=feedback_table.objects.all()
    return render(request,"admin/feedback.html",{'val':ob})

def managepolicestation(request):
    ob=policestation_table.objects.all().order_by('-id')
    return render(request,"admin/manage police station.html",{'val':ob})



def viewcrimerecord(request):
    ob=record_table.objects.all()
    return render(request,"admin/v crime record.html",{'val':ob})


def viewcriminalist(request):
    ob=criminal_table.objects.all()
    return render(request,"admin/vi criminal list.html",{'val':ob})


def addcriminallist(request):
    ob=criminal_table.objects.all()
    return render(request,"police station/add crim list.html",{'val':ob})

def criminal(request):
    nm=request.POST['textfield']
    phot=request.FILES['file']
    pla=request.POST['textfield2']
    age=request.POST['textfield3']

    fs=FileSystemStorage()
    fn=fs.save(phot.name,phot)


    oj=criminal_table()
    oj.Fname=nm
    oj.lname=nm
    oj.photo=fn
    oj.place=pla
    oj.age=age
    oj.save()

    return HttpResponse('''<script>alert("Added Successfully");window.location="/managecriminallist"</script>''')















def addpolis(request):
    return render(request,"police station/add police.html")
def police(request):
    print(request.POST)
    nme = request.POST['textfield']
    pla = request.POST['textfield2']
    phn = request.POST['phone']
    gen = request.POST['radiobutton']
    ema = request.POST['textfield4']
    use = request.POST['textfield5']
    pss = request.POST['textfield6']
    ob=login_table()
    ob.username=use
    ob.password=pss
    ob.type="police"
    ob.save()
    oj = police_table()
    oj.login = ob
    oj.Name = nme
    oj.place = pla
    oj.phone = phn
    oj.gender=gen
    oj.email=ema
    oj.policestation=policestation_table.objects.get(login__id=request.session['lid'])
    oj.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location="/managepolice"</script>''')

def managecriminallist(request):
    ob = criminal_table.objects.all()
    return render(request,"police station/manage criminallist.html",{'val':ob})

def deletecriminal(request,id):
    ob=criminal_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/managecriminallist"</script>''')

def managepolice(request):
    ob=police_table.objects.all()
    return render(request,"police station/manage police.html",{'val':ob})


def deletpolicestation(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/managepolicestation"</script>''')



def sentreport(request):
    return render(request,"police station/sent report.html")

def stationhome(request):
    return render(request,"police station/station home.html")

def taskstatus(request):
    ob=assigntask_table.objects.all()
    return render(request,"police station/task status.html",{'val':ob})

def assigntasktopolice(request):
    return render(request,"police station/tast to police.html")

def viewcomplaint(request):
    ob = complaint_table.objects.all()
    return render(request,"police station/V compliant.html",{'value':ob})

def viewreport(request):
    ob = report_table.objects.all()
    return render(request,"police station/vi report.html",{'value':ob})