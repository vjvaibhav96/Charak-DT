from django.shortcuts import render, redirect
from django.http import HttpResponse 

# Create your views here.
def doctorlogin(request):
    if request.method == "POST":
        return redirect('DoctorUserLogin')
    return render(request, 'doctor/doctorlogin.html')

def doctoruserlogin(request):
    if request.method == "POST":
        return redirect("UserOtpVerification")
    return render(request, 'doctor/doctoruserlogin.html')

def userotpverification(request):
    if request.method == "POST":
        return redirect ('DoctorMainPage')
    return render(request, 'doctor/userotpverification.html')

def doctormainpage(request):
    return render(request, 'doctor/doctormainpage.html')

def doctoraccessdata(request):
    if request.method == "POST":
        return redirect("DUserHealthData")
    return render(request, 'doctor/doctoraccessdata.html')

def duserhealthdata(request):
    return render(request, 'doctor/duserhealthdata.html')


def dedituserdata(request):
    if request.method == "POST":
        return redirect('DEditSuccess')
    return render(request, 'doctor/dedituserdata.html')

def deditsuccess(request):
    return render(request, 'doctor/deditsuccess.html')

def dprescription(request):
    if request.method == "POST":
        return redirect('DPrescriptionSuccess')
    return render(request, 'doctor/dprescription.html')

def dprescriptionsuccess(request):
    return render(request, 'doctor/dprescriptionsuccess.html')

def ddiagnostic(request):
    return render(request, 'doctor/ddiagnostic.html')
