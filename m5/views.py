from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def adminloging(request):
    return render(request,"adminloging.html")

def checklogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/homepage/")
        else:
            return redirect("/adminlogin/")

def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

def service(request):
    a = tblservice.objects.all()
    return render(request,"service.html",{'a':a})

def contact(request):
    return render(request,"contact.html")

def service_view(request):
    a=tblservice.objects.all()
    return render(request,"service_view.html",{'a':a})



def add_service(request):
    return render(request,"add_service.html")




def saveservice(request):
    a=tblservice()
    a.carservicename = request.POST.get("carservicename")
    a.servicedetails = request.POST.get("servicedetails")
    a.servicedescription = request.POST.get("servicedescription")
    a.servicetime = request.POST.get("servicetime")
    a.serviceamount = request.POST.get("serviceamount")
    a.save()
    return redirect("/service_view/")

def editdetails(request,id):
    b=tblservice.objects.get(id=id)
    return render(request,"editdetails.html",{'b':b})


def updatedetails(request,id):
    c=tblservice.objects.get(id=id)
    c.carservicename = request.POST.get("carservicename")
    c.servicedetails = request.POST.get("servicedetails")
    c.servicedescription = request.POST.get("servicedescription")
    c.servicetime = request.POST.get("servicetime")
    c.serviceamount = request.POST.get("serviceamount")
    c.save()
    return redirect("/booknow/")

def deletedetails(request,id):
    d=tblservice.objects.get(id=id)
    d.delete()
    return redirect("/service_view/")

def tech_view(request):
    a = tbltechnician.objects.all()

    return render(request,"tech_view.html",{'a':a})

def add_tech(request):
    return render(request,"add_tech.html")

def savetech(request):
    a=tbltechnician()
    a.technicianname = request.POST.get("technicianname")
    a.staffnumber =request.POST.get("staffnumber")
    a.staffexperience =request.POST.get("staff experience")
    a.staffdutytime =request.POST.get("staffdutytime")
    a.staffcode = request.POST.get("staffcode")
    a.staffamount = request.POST.get("staffamount")
    a.zip =request.POST.get("zip")
    a.save()
    return redirect("/tech_view/")

def edittech(request,id):
    b=tbltechnician.objects.get(id=id)
    return render(request,"edittech.html",{'b':b})

def updatetech(request,id):
    c=tbltechnician.objects.get(id=id)
    c.technicianname = request.POST.get("technicianname")
    c.staffnumber = request.POST.get("staffnumber")
    c.staffexperience = request.POST.get("staffexperience")
    c.staffdutytime = request.POST.get("staffdutytime")
    c.staffcode = request.POST.get("staffcode")
    c.staffamount = request.POST.get("staffamount")
    c.zip = request.POST.get("zip")
    c.save()
    return redirect("/tech_view/")

def deletetech(request,id):
    d=tbltechnician.objects.get(id=id)
    d.delete()
    return redirect("/tech_view/")


def booknow(request,id):
    a=tblservice.objects.get(id=id)
    return render(request,"booknow.html",{'a':a})

def savebooking(request,id):
    a=tblbooking

    a.firstname = request.POST.get("firsstname")
    a.lastname = request.POST.get("lastname")
    a.address = request.POST.get("address")
    a.service_id = id
    a.email = request.POST.get("email")
    a.contactno = request.POST.get("contactno")
    return redirect("paymentform",id=id)


def paymentform(request,id):
    d=tblservice.objects.get(id=id)
    return render(request,"paymentform.html",{"d":d})

def index(request):
    return redirect("/")


