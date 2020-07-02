from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login

# Create your views here.
def index(request):

    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
 # return HttpResponse("this is homepage")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def about(request):
   return render(request, 'about.html')
   # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #  return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc , date= datetime.today())
        contact.save()
        messages.success(request, "Your information has been sent successfully!")
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")