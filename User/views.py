from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def userlogin(request):
    if request.method == "POST":
        return redirect('UserHome')
    return render(request, 'user/userlogin.html')

def userhome(request):
    return render(request, 'user/userhome.html')

def accesshealthdata(request):
    if request.method == "POST":
        return redirect('HealthData')
    return render(request, 'user/accesshealthdata.html')

def healthdata(request):
    return render(request, 'user/healthdata.html')

def edithealthdata(request):
    if request.method == "POST":
        return redirect('EditHealthSuccess')
    return render(request, 'user/edithealthdata.html')

def edithealthsuccess(request):
    if request.method == "POST":
        return redirect( "{% url 'PatientHome' %}")
    return render(request, 'user/edithealthsuccess.html')

def connectsmartwatch(request):
    return render(request, 'user/connectsmartwatch.html')

def diagnostictool(request):
    return render(request, 'user/diagnostictool.html')
