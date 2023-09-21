from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Registered_Doctor
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from Manager.models import Patient_data
from .helper import MessageHandler
import pyrebase

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
# storage = firebase.storage()

# Create your views here.
def doctorlogin(request):
    if request.method == "POST":
        doctoremail = request.POST.get('doctorloginemail')
        doctorpassword = request.POST.get('doctorloginpassword')

        print('1254')
        print(doctoremail, doctorpassword)
        # authenticate the user
        duser = authenticate(username=doctoremail, password=doctorpassword)

        if duser is not None:
            print('doctor authenticated')
            print(duser.username)
            login(request, duser)
            # messages.success(request, "Successfully logged in")

            data = Registered_Doctor.objects.get(demail = doctoremail)
            global global_id
            global_id = data.doctor_id
            print(global_id)

            # user_data = Patient_data.objects.get(email = user_email)
            # global patient_id
            # patient_id = user_data.patient_id
            # print(user_data.fullname)
            return render( request, 'doctor/ddashboard.html', {'user_data' : data} )
            # return render( request, 'doctor/doctoruserlogin.html', {'user_data' : duser} )
            # return redirect('ManagerHome')
        else:
            # messages.error(request, "Invalied Credentilas")
            # return redirect("#")
            return redirect("CharakHome")

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

        duser = User.objects.create_user(username=doctoremail, password=doctorpassword, email=doctoremail, first_name=doctorfirstname)
        duser.save()

        doctor = Registered_Doctor(dfirstname=doctorfirstname, dmiddlename=doctormiddlename, dlastname=doctorlastname, dpassword=doctorpassword, dconfirmpassword=doctorcpassword, ddob=doctordob, dmobile=doctormobile, demail=doctoremail, dregistrationcouncil=doctorregistrationcouncil, dothercouncil=doctorothercouncil, dregistrationnumber=doctorregistrationnumber, duniversityname=doctoruniversity, dpassingyear=doctorpassingyear, dclinicname=doctorclinicname, dstate=doctorstate, ddistrict=doctordistrict, dcity=doctorcity, dpincode=doctorpincode, dtestfacility=doctortestfacility, ddatetime=doctordatetime, doctorflag=doctorflag)
        # doctor = Registered_Doctor (dfirstname=doctorfirstname)
        doctor.save()
        return redirect('CharakHome')
    return render(request, 'doctor/doctorsingup.html')

def doctoruserlogin(request):
    import random
    if request.method == "POST":
        userid = request.POST['userid']
        fullname = request.POST['fullname']

        global id
        id = userid
        otp= random.randint(1000, 9999)
        print(otp)
        print(id)
        verify = Patient_data.objects.get(patient_id = id)
        print(verify.otp)
        verify.otp = otp
        verify.save()
        print(verify.otp)


        messagehandler=MessageHandler(verify.phone, otp).send_otp_via_message()
        # messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()

        return redirect("UserOtpVerification")
    return render(request, 'doctor/doctoruserlogin.html')

def doctorprofile(request):
    if request.method == "POST":
        # image = request.POST['image']
        firstname = request.POST['firstname']
        lastname = request.POST['lname']
        about = request.POST['about']
        dob = request.POST['dob']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']

        updated_doctor = Registered_Doctor.objects.get(doctor_id = global_id)
        updated_doctor.dfirstname = firstname
        updated_doctor.dlastname = lastname
        updated_doctor.dabout = about
        updated_doctor.ddob = dob
        updated_doctor.dcity = city
        updated_doctor.dmobile = phone
        updated_doctor.demail = email
        updated_doctor.save()

    user_data = Registered_Doctor.objects.get(doctor_id = global_id)
    return render(request, 'doctor/doctorprofile.html', {'user_data' : user_data})

def doctordashboard(request):
    user_data = Registered_Doctor.objects.get(doctor_id = global_id)
    return render(request, 'doctor/ddashboard.html', {'user_data' : user_data})

def userotpverification(request):
    if request.method == "POST":
        userotp = request.POST['userotp']
        userotp = request.POST['userotp']
        print('userotp :', userotp)
        verify2 = Patient_data.objects.get(patient_id = id)
        print('database otp :', verify2.otp)
        
        if (userotp == verify2.otp):
            return render(request, 'doctor/duserhealthdata.html', {'userdata' : verify2})
        else:
            return redirect('DoctorUserLogin')
        
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
        userid = request.POST['userid']
        cholestrol = request.POST['cholestrol']
        bloodpressure = request.POST['bloodpressure']
        dailyexcercise = request.POST['dailyexcercise']
        cptype = request.POST['cptype']
        glucose = request.POST['glucose']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        prediabetic = request.POST['prediabetic']
        dpf = request.POST['dpf']
        prescription = request.POST['prescription']

        doctoruserdata = Patient_data.objects.get(patient_id = userid)
        doctoruserdata.cholestrol = cholestrol
        doctoruserdata.bloodpressure = bloodpressure
        doctoruserdata.dailyexercise = dailyexcercise
        doctoruserdata.chestpaintype = cptype
        doctoruserdata.glucosevalue = glucose
        doctoruserdata.insulinvalue = insulin
        doctoruserdata.bmi = bmi
        doctoruserdata.prediabetic = prediabetic
        doctoruserdata.dpf = dpf
        doctoruserdata.prescription = prescription

        doctoruserdata.save()
        return redirect('DEditSuccess')
    
    return render(request, 'doctor/dedituserdata.html')

def deditsuccess(request):
    return render(request, 'doctor/deditsuccess.html')

def dprescription(request):
    if request.method == "POST":
        userid = request.POST['userid']
        fullname = request.POST['fullname']
        prescription  = request.POST['prescription']

        userpres = Patient_data.objects.get(patient_id = userid)
        userpres.prescription = prescription
        userpres.save()
        return redirect('DPrescriptionSuccess')
    return render(request, 'doctor/dprescription.html')

def dprescriptionsuccess(request):
    return render(request, 'doctor/dprescriptionsuccess.html')

def ddiagnostic(request):
    return render(request, 'doctor/ddiagnostic.html')

def doctorctscan2d(request):
    if request.method == "POST":
        print(1)
        userid = request.POST['userid']
        patientname = request.POST['patientname']
        # userid = request.POST['userid']
        # userid = request.POST['userid']
        print(userid, patientname)
        data_ref = database.child('data').child(patientname)
        
        # Read data from the reference
        data = data_ref.get().val()

        # Check if data exists
        if data is not None:
        # Data exists, you can access it as a dictionary
            # print('Data:', data['-NeqJvr9mWRJGRWl4eV3']['path'])
            for value in data.values():
                path = value['path']
                # print('Path :', value['path'])
                return render(request, 'doctor/ctscan2dsuccess.html', {'path': path})
                # return redirect(f'https://easiofydicomviewer-iit.netlify.app/?Patient={path}')
        else:
            print('No data found at the specified location.')
         
    return render(request, 'doctor/ctscan2d.html')

def doctorctscan3d(request):
    if request.method == "POST":
        print(1)
        userid = request.POST['userid']
        patientname = request.POST['patientname']
        # userid = request.POST['userid']
        # userid = request.POST['userid']
        print(userid, patientname)
        data_ref = database.child('data').child(patientname)
        
        # Read data from the reference
        data = data_ref.get().val()

        # Check if data exists
        if data is not None:
        # Data exists, you can access it as a dictionary
            # print('Data:', data['-NeqJvr9mWRJGRWl4eV3']['path'])
            for value in data.values():
                path = value['path3d']
                print(path)
                # print('Path :', value['path'])
                return render(request, 'doctor/ctscan3dsuccess.html', {'path': path})
                # return redirect(f'https://easiofydicomviewer-iit.netlify.app/?Patient={path}')
        else:
            print('No data found at the specified location.')
         
    return render(request, 'doctor/ctscan3d.html')

def doctorlogout(request):
    logout(request)
    return redirect('CharakHome')