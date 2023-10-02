from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registered_Pathologist
import datetime
import pyrebase
from google.cloud import storage
from google.auth import impersonated_credentials
import firebase_admin
from firebase_admin import credentials
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Manager.models import Patient_data
from Doctor.helper import MessageHandler
from User.models import vitals_data

# Config file vaibhav firebase
# config = {
#     'apiKey' : "AIzaSyDVj6Orit--mR0bcfhNX_3r_y2MPdg6s_A",
#     'authDomain' : "test2-f9b1a.firebaseapp.com",
#     'databaseURL' : "https://test2-f9b1a-default-rtdb.firebaseio.com/",
#     'projectId' : "test2-f9b1a",
#     'storageBucket' : "test2-f9b1a.appspot.com",
#     'messagingSenderId' : "551779111637",
#     'appId' : "1:551779111637:web:f54aff6975df6c6c1d485c",
#     'measurementId' : "G-CDCWYBZN16"
# };
# Config file dikshant firebase
config = {
 'apiKey': "AIzaSyD4Kk5ckPMU7DCAQGF54NvYePXed3w9uT0",
 'authDomain': "charak-e18cb.firebaseapp.com",
 'databaseURL': "https://charak-e18cb-default-rtdb.firebaseio.com",
 'projectId': "charak-e18cb",
 'storageBucket': "charak-e18cb.appspot.com",
 'messagingSenderId': "629360219131",
 'appId': "1:629360219131:web:906a2ccdac0abdd904715e",
 'measurementId': "G-PLJNWBCS6Y"
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
        pathoemail = request.POST.get('pathologinemail')
        pathopassword = request.POST.get('pathologinpassword')

        puser = authenticate(username = pathoemail, password=pathopassword)
        if puser is not None:
            login(request, puser)
            patho = Registered_Pathologist.objects.get(pemail = pathoemail)
            global pid
            pid = patho.patho_id
            print(pid)
            print(patho.pfirstname)
            return render(request, 'pathologist/pathoprofile.html', {'user_data' : patho})
        else:
            return render(request, 'pathologist/pathologin.html')
    return  render(request, 'pathologist/pathologin.html')

def pathohomepage(request):
    if request.method == "POST":
        return redirect('PathoUserLogin')
    return render(request, 'pathologist/pathohomepage.html')

def pathouserlogin(request):
    import random
    if request.method == "POST":
        userid = request.POST['userid']
        patientname = request.POST['patientname']

        global uid
        otp= random.randint(1000, 9999)
        user_instance = Patient_data.objects.get(patient_id = userid)
        user_instance.otp = otp
        uid = user_instance.patient_id
        user_instance.save()
        messagehandler=MessageHandler(user_instance.phone, otp).send_otp_via_message()

        return render(request, 'pathologist/pathouserotp.html')
    return render(request, 'pathologist/pathouserlogin.html')

def pathouserotp(request):
    
    if request.method == "POST":
        otp = request.POST['otp']
        user_otp = Patient_data.objects.get(patient_id = uid)

        if (otp == user_otp.otp):
            return render(request, 'pathologist/pathouserdata.html', {'user_data': user_otp})
        else:
            return render(request, 'pathologist/pathouserotp.html')
    return render(request, 'pathologist/pathouserotp.html')

def pathoaccess(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)

    if request.method == "POST":
        userid = request.POST['userid']
        fullname = request.POST['fullname']

        userdata = Patient_data.objects.get(patient_id = userid)

        return render(request, 'pathologist/pathouserdata.html', {'userdata' : userdata })
    return render(request, 'pathologist/pathoaccess.html')

def pathouserdata(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)

    return render(request, 'pathologist/pathouserdata.html')

def pathoedit(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)
    if request.method == "POST":
        userid = request.POST['userid']
        bodytemperature = request.POST['bodytemperature']
        pulserate = request.POST['pulserate']
        respiratoryrate = request.POST['respiratoryrate']
        bp = request.POST['bp']
        spo2 = request.POST['spo2']
        weight = request.POST['weight']
        bloodsugarfbs = request.POST['bloodsugarfbs']
        bloodsugarrbs = request.POST['bloodsugarrbs']
        datetime1 = request.POST['datetime1']
        # report = request.FILES.get('report')
        # xray = request.FILES.get('xray')

        pd = Patient_data.objects.get(patient_id = userid)
        v_data = vitals_data(patient_id=pd, bodytemperature=bodytemperature, pulserate=pulserate, respiratoryrate=respiratoryrate, 
        bp=bp, spo2=spo2, weight=weight, bloodsugarfbs=bloodsugarfbs, bloodsugarrbs=bloodsugarrbs, datetime=datetime1)
        v_data.save()
        
        return redirect('PathoEditSuccess')
    
    return render(request, 'pathologist/pathoedit.html')

def pathoeditsuccess(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)

    return render(request, 'pathologist/pathoeditsuccess.html')

def pathotodoctorpres(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)

    return render(request, 'pathologist/pathotodoctorpres.html')

def pathotodocsuccess(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)

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

        puser = User.objects.create_user(username=pathoemail, password=pathopassword, email=pathoemail, first_name=pathofirstname)  
        puser.save()

        return redirect('CharakHome')
    return render(request, 'pathologist/pathosingup.html')

def pathoesiofy2d(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        firstname = request.POST.get('esiofyuserfirst')
        foldername = request.POST.get('esiofyuserfolder')
        patientname = request.POST.get('esiofypatientname')

        patient_obj = Patient_data.objects.get(patient_id  = userid)
        patient_obj.esio_patient_name = patientname
        patient_obj.esio_folder_name = foldername
        patient_obj.esio_first_name = firstname 

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
        # print(uploaded_file_url)
        data = {
            'firstname': firstname,
            'foldername' : foldername,
            'path' : f'{patientname}/{foldername}',
            # 'path3d' : f'{patientname}/{foldername}/{uploaded_file}'
            # 'file_path' : storage.child(f'{patientname}').child(f'{foldername}')
            # 'file_path' : uploaded_file_url
        }
        user = database.child("data").child(patientname).push(data)
        uploaded_file_url = []
        return render(request, 'pathologist/pathoesiofysuccess.html')
     
    return render(request, 'pathologist/pathoesiofy2d.html')

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
        # print(uploaded_file_url)
        data = {
            'firstname': firstname,
            'foldername' : foldername,
            'path' : f'{patientname}/{foldername}',
            'path3d' : f'{patientname}/{foldername}/{uploaded_file}'
            # 'file_path' : storage.child(f'{patientname}').child(f'{foldername}')
            # 'file_path' : uploaded_file_url
        }
        user = database.child("data").child(patientname).push(data)
        uploaded_file_url = []
        return render(request, 'pathologist/pathoesiofysuccess.html')
     
    return render(request, 'pathologist/pathoesiofy.html')

def pathodashboard(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)

    return render(request, 'pathologist/pathodashboard.html', {'patho_data' : patho_data})
    # return render(request, 'pathologist/pathodashboard.html', {'patho_data' : patho_data})

def pathoprofile(request):
    patho_data = Registered_Pathologist.objects.get(patho_id = pid)
    if request.method== "POST":
        # image = request.POST['image']
        pathoid = request.POST['pathoid']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        about = request.POST['about']
        dob = request.POST['dob']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']

        profile_obj = Registered_Pathologist.objects.get(patho_id = pathoid)
        profile_obj.pfirstname = firstname
        profile_obj.plastname = lastname
        profile_obj.pabout = about
        profile_obj.pdob = dob
        profile_obj.pcity = city
        profile_obj.pemail = email
        profile_obj.pmobile = phone

        profile_obj.save()
        return render(request, 'pathologist/pathoprofile.html', {'user_data' : profile_obj})

    return render(request, 'pathologist/pathoprofile.html', {'user_data' : patho_data})

def pathologout(request):
    logout(request)
    return redirect('CharakHome')

