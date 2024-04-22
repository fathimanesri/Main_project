from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class user_table(models.Model):
    login=models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=25)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=25)

class complaint_table(models.Model):
    complaint_details = models.CharField(max_length=100)
    date=models.DateField()
    reply = models.CharField(max_length=100)
    userid=models.ForeignKey(user_table,on_delete=models.CASCADE)
    policestation=models.ForeignKey(policestation_table,on_delete=models.CASCADE)
    report=models.CharField(max_length=100)

class policestation_table(models.Model):
    login=models.ForeignKey(login_table,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email=models.CharField(max_length=25)


class criminal_table(models.Model):
    Fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    photo=models.FileField()
    place = models.CharField(max_length=100)
    age=models.IntegerField()

class police_table(models.Model):
    login=models.ForeignKey(login_table,on_delete=models.CASCADE)
    policestation=models.ForeignKey(policestation_table,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    gender=models.CharField(max_length=25)
    email=models.CharField(max_length=25)

class feedback_table(models.Model) :
    feedback=models.CharField(max_length=100)
    date=models.DateField()
    feedbacktext=models.CharField(max_length=100)
    rating=models.FloatField()
    userid=models.ForeignKey(user_table,on_delete=models.CASCADE)

class assigntask_table(models.Model):
    policeid=models.ForeignKey(police_table,on_delete=models.CASCADE)
    task=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=100)

class report_table(models.Model):
    assigntask=models.ForeignKey(assigntask_table,on_delete=models.CASCADE)
    report=models.FileField()
    date=models.DateField()







