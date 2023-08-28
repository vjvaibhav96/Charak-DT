from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return  render(request, 'pathologist/index.html')

def pathologin(request):
    if request.method == "POST":
        return redirect('PathoHomePage')
    return  render(request, 'pathologist/pathologin.html')

def pathohomepage(request):
    if request.method == "POST":
        return redirect('PathoUserLogin')
    return render(request, 'pathologist/pathohomepage.html')

def pathouserlogin(request):
    if request.method == "POST":
        return redirect('PathoUserOtp')
    return render(request, 'pathologist/pathouserlogin.html')

def pathouserotp(request):
    return render(request, 'pathologist/pathouserotp.html')

def pathoaccess(request):
    if request.method == "POST":
        return redirect('PathoUserData')
    return render(request, 'pathologist/pathoaccess.html')

def pathouserdata(request):
    return render(request, 'pathologist/pathouserdata.html')

def pathoedit(request):
    if request.method == "POST":
        return redirect('PathoEditSuccess')
    return render(request, 'pathologist/pathoedit.html')

def pathoeditsuccess(request):
    return render(request, 'pathologist/pathoeditsuccess.html')

def pathotodoctorpres(request):
    return render(request, 'pathologist/pathotodoctorpres.html')

def pathotodocsuccess(request):
    return render(request, 'pathologist/pathotodocsuccess.html')


