from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registered_Pathologist
import datetime

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

def pathosingup(request):
    if request.method == "POST": 
        pathofirstname = request.POST.get('pathofirstname')
        pathomiddlename = request.POST.get('pathomiddlename')
        patholastname = request.POST.get('patholastname')
        pathodob = request.POST.get('pathodob')
        pathomobile = request.POST.get('pathomobile')
        pathoemail = request.POST.get('pathoemail')
        pathopassword = request.POST.get('pathopassword')
        pathoconfirmpassword = request.POST.get('pathoconfirmpassword')
        pathoregistrationnumber = request.POST.get('pathoregistrationnumber')
        pathoregistrationcouncil = request.POST.get('pathoregistrationcouncil')
        pathovalidfrom = request.POST.get('pathovalidfrom')
        pathovalidto = request.POST.get('pathovalidto')
        pathodistrict =  request.POST.get('pathodistrict')
        pathostate = request.POST.get('pathostate')
        pathodistrict = request.POST.get('pathodistrict')
        pathocity = request.POST.get('pathocity')
        pathopin = request.POST.get('pathopin')
        pathotestfacility = request.POST.get('pathotestfacility')
        pathodatetime = datetime.datetime.now()
        pathoflag = 0

        patho = Registered_Pathologist(pfirstname = pathofirstname, pmiddlename=pathomiddlename, plastname=patholastname, pdob = pathodob, ppassword=pathopassword, pconfirmpassword=pathoconfirmpassword, pmobile = pathomobile, pemail=pathoemail, pregistrationnumber = pathoregistrationnumber, pvalidfrom = pathovalidfrom, pvalidto = pathovalidto, pstate = pathostate, pdistrict=pathodistrict, pcity = pathocity, ppin = pathopin, ptestfacility=pathotestfacility, pdatetime=pathodatetime, pregistrationcouncil=pathoregistrationcouncil, pathoflag=pathoflag)
        patho.save()
       
        return redirect('CharakHome')
    return render(request, 'pathologist/pathosingup.html')


