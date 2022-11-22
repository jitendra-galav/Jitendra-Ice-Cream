from operator import index
from urllib import request
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# def index(request):
#     # return HttpResponse("this is homepage")
#     context={
#         'variable' : "this is sent",
#         'variable1' : " this is greate jitu",
#         "variable2": " this is greate game"

#     }
#     return render(request,'index.html' , context)
def index(request):
    # messages.success(request,'this is a test meaasgae')
    return render(request,'index.html' )

def about(request):
     return render(request,'about.html' )
    # return HttpResponse("this is about homepage")

def services(request):
     return render(request,'services.html' )
    # return HttpResponse("this is services homepage")

def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Messsage Has Been Sent !')
    return render(request,'contact.html')
    # return HttpResponse("this is contact homepage")
# Create your views here.
