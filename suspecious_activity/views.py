import json
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from suspecious_activity.models import *


def login(request):
    return render(request,"login_index.html")


def logout(request):
    auth.logout(request)
    return render(request,'login_index.html')



def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=username,password=password)
        if ob.type=='admin' :
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("success");window.location="/admin"</script>''')

        elif ob.type == 'station':
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("success");window.location="/stationhome"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username");window.location="/"</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert("invalid username");window.location="/"</script>''')


@login_required(login_url='/')


def addpolicestation(request):
    return render(request,"admin/add police station.html")
@login_required(login_url='/')

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
    return HttpResponse('''<script>alert("Added Successfully");window.location="/managepolicestation#constructions"</script>''')

@login_required(login_url='/')

def admin(request):
    return render(request,"admin/index.html")

@login_required(login_url='/')

def feedback(request):
    ob=feedback_table.objects.all()
    return render(request,"admin/feedback.html",{'val':ob})

@login_required(login_url='/')

def feedbacksrch(request):
    date=request.POST['textfield']
    ob=feedback_table.objects.filter(date=date)
    return render(request,"admin/feedback.html",{'val':ob})

@login_required(login_url='/')

def managepolicestation(request):
    ob=policestation_table.objects.all().order_by('-id')
    return render(request,"admin/manage police station.html",{'val':ob})


@login_required(login_url='/')



def editstation(request, id):
    ob = police_table.objects.get(id=id)
    request.session["po_id"] = id
    return render(request,"admin/editpolice station.html",{'val': ob})
@login_required(login_url='/')

def police_station (request):
    nm=request.POST['textfield']
    ph=request.POST['textfield2']
    pl=request.POST['textfield3']
    em=request.POST['textfield4']
    ob=policestation_table.objects.get(id=request.session["po_id"])
    ob.place=pl
    ob.Name=nm
    ob.phone=ph
    ob.email=em
    ob.save()
    return HttpResponse('''<script>alert("edited Successfully");window.location="/managepolicestation#constructions"</script>''')

@login_required(login_url='/')



def viewcrimerecord(request):
    ob=record_table.objects.all()
    ob1=policestation_table.objects.all()
    return render(request,"admin/v crime record.html",{'val':ob,"anu":ob1})
@login_required(login_url='/')

def viewcrimerecordsrch(request):
    a=request.POST['select']
    ob=record_table.objects.filter(policeid__policestation__id=a)
    ob1=policestation_table.objects.all()

    return render(request,"admin/v crime record.html",{'val':ob,"anu":ob1,'a':int(a)})






@login_required(login_url='/')

def viewcriminalist(request):
    ob=criminal_table.objects.all()
    ob1=policestation_table.objects.all()
    return render(request,"admin/vi criminal list.html",{'val':ob,'val1':ob1})

@login_required(login_url='/')


def viewcriminalistsrch(request):
    a=request.POST['select']
    ob=criminal_table.objects.filter(policestation_id=a)
    ob1=policestation_table.objects.all()

    return render(request,"admin/vi criminal list.html",{'val':ob,'val1':ob1,'a':int(a)})
@login_required(login_url='/')


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
    oj.policestation=policestation_table.objects.get(login__id=request.session['lid'])
    oj.save()

    return HttpResponse('''<script>alert("Added Successfully");window.location="/managecriminallist#constructions"</script>''')
@login_required(login_url='/')


def addpolis(request):
    return render(request,"police station/add police.html")

@login_required(login_url='/')

def editpolis(request, id):
    ob = police_table.objects.get(id=id)
    request.session["police_id"]=id
    return render(request,"police station/addeditpolice.html",{'val': ob})

@login_required(login_url='/')

def edit_post(request):
    try:
        nme = request.POST['textfield']
        pla = request.POST['textfield2']
        phn = request.POST['phone']
        gen = request.POST['radiobutton']
        ema = request.POST['textfield4']

        oj = police_table.objects.get(id=request.session["police_id"])
        oj.Name = nme
        oj.place = pla
        oj.phone = phn
        oj.gender = gen
        oj.email = ema
        oj.policestation = policestation_table.objects.get(login__id=request.session['lid'])
        oj.save()
        return HttpResponse('''<script>alert("Added Successfully");window.location="/managepolice#constructions"</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid ");window.location="/managepolice#constructions"</script>''')

@login_required(login_url='/')

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
    return HttpResponse('''<script>alert("Added Successfully");window.location="/managepolice#constructions"</script>''')

@login_required(login_url='/')

def managecriminallist(request):
    ob = criminal_table.objects.filter(policestation__login__id=request.session['lid'])
    return render(request,"police station/manage criminallist.html",{'val':ob})

@login_required(login_url='/')


def managecriminallistsrch(request):
    name=request.POST['textfield']
    ob = criminal_table.objects.filter(Fname__icontains=name)
    return render(request,"police station/manage criminallist.html",{'val':ob})




@login_required(login_url='/')


def editcriminal(request, id):
    request.session['c_id'] = id
    ob = criminal_table.objects.get(id=id)
    return render(request,"police station/editcriminallist.html",{'val': ob})

@login_required(login_url='/')

def  editcriminals(request):
    try:
        nm=request.POST['textfield']
        phot=request.FILES['file']
        pla=request.POST['textfield2']
        age=request.POST['textfield3']

        fs=FileSystemStorage()
        fn=fs.save(phot.name,phot)
        oj=criminal_table.objects.get(id=request.session['c_id'])
        oj.Fname=nm
        oj.lname=nm
        oj.photo=fn
        oj.place=pla
        oj.age=age
        oj.policestation = policestation_table.objects.get(login__id=request.session['lid'])

        oj.save()
        return HttpResponse('''<script>alert("Added Successfully");window.location="/managecriminallist#constructions"</script>''')
    except:
        nm = request.POST['textfield']
        pla = request.POST['textfield2']
        age = request.POST['textfield3']

        oj = criminal_table.objects.get(id=request.session['c_id'])
        oj.Fname = nm
        oj.lname = nm
        oj.place = pla
        oj.age = age
        oj.policestation = policestation_table.objects.get(login__id=request.session['lid'])

        oj.save()
        return HttpResponse('''<script>alert("Added Successfully");window.location="/managecriminallist#constructions"</script>''')

@login_required(login_url='/')

def deletecriminal(request,id):
    ob=criminal_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/managecriminallist#constructions"</script>''')

@login_required(login_url='/')

def managepolice(request):
    ob=police_table.objects.filter(policestation__login__id=request.session['lid'])
    return render(request,"police station/manage police.html",{'val':ob})

@login_required(login_url='/')

def managepolicesrch(request):
    name=request.POST['textfield']
    ob=police_table.objects.filter(Name__icontains=name)

    return render(request,"police station/manage police.html",{'val':ob})

@login_required(login_url='/')


def deletpolice(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/managepolicestation#constructions"</script>''')
@login_required(login_url='/')


def deletpolicestation(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/managepolicestation#constructions"</script>''')

@login_required(login_url='/')


def sentreport(request,id):
    request.session['c_id']=id
    return render(request,"police station/sent report.html")

@login_required(login_url='/')

def reply_post(request):
    re = request.POST['textfield']
    rep = request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(rep.name,rep)
    ob=complaint_table.objects.get(id=request.session['c_id'])
    ob.reply = re
    ob.report=fn
    ob.save()
    return HttpResponse('''<script>alert("sented Successfully");window.location="viewcomplaint#constructions"</script>''')

@login_required(login_url='/')

def stationhome(request):
    return render(request,"police station/index.html")

@login_required(login_url='/')

def taskstatus(request):
    ob1=police_table.objects.filter(policestation__login__id=request.session['lid'])
    ob=assigntask_table.objects.filter(policeid__policestation__login__id=request.session['lid'])
    return render(request,"police station/task status.html",{'val':ob,'val1':ob1})

@login_required(login_url='/')

def taskstatussrch(request):
    a=request.POST['select']
    ob1=police_table.objects.filter(policestation__login__id=request.session['lid'])
    ob=assigntask_table.objects.filter(policeid__policestation__login__id=request.session['lid'],policeid__id=a)
    return render(request,"police station/task status.html",{'val':ob,'val1':ob1,"a":int(a)})

@login_required(login_url='/')




def assigntasktopolice(request):
    p_obj = police_table.objects.filter(policestation__login__id=request.session['lid'])
    return render(request,"police station/tast to police.html", {'val': p_obj})

@login_required(login_url='/')

def assigntask(request):
    po = request.POST['select']
    ta = request.POST['textfield']

    ob = assign_table()
    ob.policeid = police_table.objects.get(id=po)
    ob.task=ta
    ob.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location="stationhome#constructions"</script>''')

@login_required(login_url='/')

def viewcomplaint(request):
    ob = complaint_table.objects.filter(policestation__login__id=request.session['lid'])
    return render(request,"police station/V compliant.html",{'value':ob})

@login_required(login_url='/')


def viewcomplaintsrch(request):
    date=request.POST['textfield']
    ob = complaint_table.objects.filter(date=date)
    return render(request,"police station/V compliant.html",{'value':ob})


@login_required(login_url='/')



def viewreport(request):
    ob = report_table.objects.filter(policeid__policestation__login__id=request.session['lid'])
    return render(request,"police station/vi report.html",{'value':ob})




# %%%%%%%%%%%%%%%%%%%%%%%%%%webservice%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





def send_complaints(request):
    complaint=request.POST['complaint']
    id=request.POST['lid']
    comp_ob = complaint_table()
    comp_ob.complaint=complaint
    comp_ob.date= datetime.now()
    comp_ob.reply='pending'
    comp_ob.USER=user_table.objects.get(LOGIN=id)
    comp_ob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)







def sendfeedback(request):
    feedback=request.POST['feedback']
    rating=request.POST['rating']
    uid = request.POST["uid"]

    complaint_obj = feedback_table()
    complaint_obj.userid = user_table.objects.get(LOGIN__id=uid)
    complaint_obj.feedback = feedback
    complaint_obj.rating = rating
    complaint_obj.date=datetime.today()
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def logincodes(request):
    print(request.POST)
    un = request.POST['username']
    pw = request.POST['password']
    ob = login_table.objects.get(username=un, password=pw)
    if ob is None:
        ob1 = {"task": "invalid"}
    else:
        ob1 = {"task": "valid", "lid": ob.id, "type": ob.type}
    l = json.dumps(ob1)
    return HttpResponse(l)


def registration(request):
    try:
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        add = request.POST['pin']

        phone = request.POST['mobile']
        gender = request.POST['gender']
        email_id = request.POST['email']
        uname = request.POST['username']
        passwd = request.POST['password']
        lat = request.POST['place']
        long = request.POST['post']

        ob = login_table.objects.filter(username=uname)
        if len(ob) == 0:
            lob = login_table()
            lob.username = uname
            lob.password = passwd
            lob.type = 'user'
            lob.save()

            userob = user_table()
            userob.fname = Fname
            userob.lname = Lname
            userob.pin = add
            userob.phone = phone
            userob.gender = gender
            userob.email = email_id

            userob.LOGIN = lob
            userob.place = lat
            userob.post = long
            userob.save()
            data = {"task": "success"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            print("################ same passs", )
            data = {"task": "invalid"}
            r = json.dumps(data)
            return HttpResponse(r)
    except Exception as e:
        print("$$$$$$$$$$$$$ except", e)
        data = {"task": "error"}
        r = json.dumps(data)
        return HttpResponse(r)

