from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime

# Create your views here.
context ={
        'variable':"THis is Sent."
    }

def index(request):
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html',context)

def services(request):
    return render(request,'services.html',context)

def cafe(request):
    return render(request,'services1.html',context)

def contact(request):
    if request.method == "POST":
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        
        contact = Contact(email=email,desc=desc)
        contact.save()
    return render(request,'contact.html',context)