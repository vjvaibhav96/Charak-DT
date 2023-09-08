from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registered_Pathologist
import datetime
import pyrebase
from google.cloud import storage
from google.auth import impersonated_credentials
import firebase_admin
from firebase_admin import credentials

config = {
    'apiKey' : "AIzaSyDVj6Orit--mR0bcfhNX_3r_y2MPdg6s_A",
    'authDomain' : "test2-f9b1a.firebaseapp.com",
    'databaseURL' : "https://test2-f9b1a-default-rtdb.firebaseio.com/",
    'projectId' : "test2-f9b1a",
    'storageBucket' : "test2-f9b1a.appspot.com",
    'messagingSenderId' : "551779111637",
    'appId' : "1:551779111637:web:f54aff6975df6c6c1d485c",
    'measurementId' : "G-CDCWYBZN16"
};

firebase = pyrebase.initialize_app(config)
database = firebase.database()
storage = firebase.storage()

auth = firebase.auth()

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

def pathoesiofy(request):
    if request.method == "POST":
        firstname = request.POST.get('esiofyuserfirst')
        foldername = request.POST.get('esiofyuserfolder')
        patientname = request.POST.get('esiofypatientname')
        # print(files)

        # current_directory = os.path.dirname(os.path.realpath(__file__))
        # json_file_path = os.path.join(current_directory, 'info.json')
        # cred = credentials.Certificate(json_file_path)
        # firebase_admin.initialize_app(cred)
        # bucket_url = "gs://test2-f9b1a.appspot.com"
        # bucket_name = "test2-f9b1a.appspot.com"
        # storage_client = storage.Client(credentials=None)
        # bucket = storage_client.get_bucket(bucket_name)

        # getting all the files from the form
        uploaded_files = request.FILES.getlist('esiofypatientfiles')
        uploaded_file_url = []

        # iterating through each file for uploading
        for uploaded_file in uploaded_files:
            try:
                destination_path = f"{patientname}/{foldername}/{uploaded_file.name}"
                storage.child(destination_path).put(uploaded_file)
                file_url = storage.child(f'{patientname}').child(f'{foldername}').get_url(None)
                uploaded_file_url.append(file_url)
            except Exception as e:
               print(f"Error uploading file: {str(e)}")
        print(uploaded_file_url)

        data = {
            'firstname': firstname,
            'foldername' : foldername,
            'file_path' : storage.child(f'{patientname}').child(f'{foldername}')
            # 'file_path' : uploaded_file_url
        }
        user = database.child("data").child(patientname).push(data)
        uploaded_file_url = []
        return HttpResponse("Files uploaded successfully!")
     
    return render(request, 'pathologist/pathoesiofy.html')


