from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Registered_Doctor
import datetime

# Create your views here.
def doctorlogin(request):
    if request.method == "POST":
        return redirect('DoctorUserLogin')
    return render(request, 'doctor/doctorlogin.html')

def doctorsingup(request):
    if request.method == "POST":
        doctorfirstname = request.POST.get('doctorfirstname')
        doctormiddlename = request.POST.get('doctormiddlename')
        doctorlastname = request.POST.get('doctorlastname')
        doctordob = request.POST.get('doctordob')
        doctormobile = request.POST.get('doctormobile')
        doctoremail = request.POST.get('doctoremail')
        doctorpassword = request.POST.get('doctorpassword')
        doctorcpassword = request.POST.get('doctorcpassword')
        doctorregistrationcouncil = request.POST.get('doctorregistrationcouncil')
        doctorothercouncil = request.POST.get('other_council')
        doctorregistrationnumber = request.POST.get('doctorregistrationnumber')
        doctoruniversity = request.POST.get('doctoruniversity')
        doctorpassingyear = request.POST.get('doctorpassingyear')
        doctorclinicname = request.POST.get('doctorclinicname')
        doctorstate = request.POST.get('doctorstate')
        doctordistrict = request.POST.get('doctordistrict')
        doctorcity = request.POST.get('doctorcity')
        doctorpincode = request.POST.get('doctorpincode')
        doctortestfacility = request.POST.get('doctortestfacility')
        doctordatetime = datetime.datetime.now()
        doctorflag = 0

        doctor = Registered_Doctor(dfirstname=doctorfirstname, dmiddlename=doctormiddlename, dlastname=doctorlastname, dpassword=doctorpassword, dconfirmpassword=doctorcpassword, ddob=doctordob, dmobile=doctormobile, demail=doctoremail, dregistrationcouncil=doctorregistrationcouncil, dothercouncil=doctorothercouncil, dregistrationnumber=doctorregistrationnumber, duniversityname=doctoruniversity, dpassingyear=doctorpassingyear, dclinicname=doctorclinicname, dstate=doctorstate, ddistrict=doctordistrict, dcity=doctorcity, dpincode=doctorpincode, dtestfacility=doctortestfacility, ddatetime=doctordatetime, doctorflag=doctorflag)
        # doctor = Registered_Doctor (dfirstname=doctorfirstname)
        doctor.save()
        return redirect('CharakHome')
    return render(request, 'doctor/doctorsingup.html')

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
