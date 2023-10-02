from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Registered_Doctor
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from Manager.models import Patient_data
from User.models import vitals_data, exercise_data, medication_data, eating_habits_data, eating_habits_other, todays_feel_data, health_condition_data
from .helper import MessageHandler
import pyrebase
from django.conf import settings
import pickle
import os
import numpy as np

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
            return render( request, 'doctor/doctorprofile.html', {'user_data' : data} )
            # return render( request, 'doctor/ddashboard.html', {'user_data' : data} )
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

# global var
# var = int(0)

def dprescription3d(request):
    if request.method == "POST":
        global var
        var = request.POST['var']
        userid = request.POST['userid']

        obj = Patient_data.objects.get(patient_id = userid)
        obj.threed = var
        obj.save()

        return redirect('DPrescriptionSuccess')

    return render(request, 'doctor/dprescription3d.html')

def accessregisteredpatients(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        verify2 = Patient_data.objects.get(patient_id = userid)

        user_hdata = Patient_data.objects.get(patient_id=userid)
        user_vital_latest = vitals_data.objects.latest('datetime')
        user_vital = vitals_data.objects.filter(patient_id=user_hdata)
        user_exercises = exercise_data.objects.filter(patient_id=user_hdata)
        user_medications = medication_data.objects.filter(patient_id=user_hdata)
        user_eating = eating_habits_other.objects.filter(patient_id=user_hdata)
        user_health_condition = health_condition_data.objects.filter(patient_id=user_hdata)
        user_today = todays_feel_data.objects.filter(patient_id=user_hdata)
        var = int(user_hdata.threed)

        context = {
                'user_hdata' : user_hdata,
                'user_vital_latest' : user_vital_latest,
                'user_vital' : user_vital,
                'user_exercises' : user_exercises,
                'user_medications' : user_medications,
                'user_eating' : user_eating,
                'user_health_condition' : user_health_condition,
                'user_today' : user_today,
                'userdata' : verify2,
                'var' : var
            }
        print('var :', var)
        print('vartype :', type(var))
        return render(request, 'doctor/duserhealthdata.html', context=context)

    return render(request, 'doctor/accessregisteredpatients.html')

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
            user_hdata = Patient_data.objects.get(patient_id=id)
            user_vital_latest = vitals_data.objects.latest('datetime')
            user_vital = vitals_data.objects.filter(patient_id=user_hdata)
            user_exercises = exercise_data.objects.filter(patient_id=user_hdata)
            user_medications = medication_data.objects.filter(patient_id=user_hdata)
            user_eating = eating_habits_other.objects.filter(patient_id=user_hdata)
            user_health_condition = health_condition_data.objects.filter(patient_id=user_hdata)
            user_today = todays_feel_data.objects.filter(patient_id=user_hdata)
            var = int(user_hdata.threed)

            context = {
                'user_hdata' : user_hdata,
                'user_vital_latest' : user_vital_latest,
                'user_vital' : user_vital,
                'user_exercises' : user_exercises,
                'user_medications' : user_medications,
                'user_eating' : user_eating,
                'user_health_condition' : user_health_condition,
                'user_today' : user_today,
                'userdata' : verify2,
                'var': var
            }
            return render(request, 'doctor/duserhealthdata.html', context=context)
        else:
            return redirect('DoctorUserLogin')
        
    return render(request, 'doctor/userotpverification.html')

def doctormainpage(request):
    return render(request, 'doctor/doctormainpage.html')


def doctoraccessdata(request):
    if request.method == "POST":
        patient_id = request.POST['userid']

        global patientid
        patientid = patient_id
        print('patientid for doctor :', patientid)
        return redirect("DUserHealthData")
    return render(request, 'doctor/doctoraccessdata.html')

def duserhealthdata(request):
    print('patient id received :', patientid)
    user_hdata = Patient_data.objects.get(patient_id=patientid)
    user_vital_latest = vitals_data.objects.latest('datetime')
    user_vital = vitals_data.objects.filter(patient_id=user_hdata)
    user_exercises = exercise_data.objects.filter(patient_id=user_hdata)
    user_medications = medication_data.objects.filter(patient_id=user_hdata)
    user_eating = eating_habits_other.objects.filter(patient_id=user_hdata)
    user_health_condition = health_condition_data.objects.filter(patient_id=user_hdata)
    user_today = todays_feel_data.objects.filter(patient_id=user_hdata)
    var = int(user_hdata.threed)

    context = {
        'user_hdata' : user_hdata,
        'user_vital_latest' : user_vital_latest,
        'user_vital' : user_vital,
        'user_exercises' : user_exercises,
        'user_medications' : user_medications,
        'user_eating' : user_eating,
        'user_health_condition' : user_health_condition,
        'user_today' : user_today,
        'var' : var
    }
    return render(request, 'doctor/duserhealthdata.html', context=context)


def dedituserdata(request):
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

        pd = Patient_data.objects.get(patient_id = userid)
        v_data = vitals_data(patient_id=pd, bodytemperature=bodytemperature, pulserate=pulserate, respiratoryrate=respiratoryrate, 
        bp=bp, spo2=spo2, weight=weight, bloodsugarfbs=bloodsugarfbs, bloodsugarrbs=bloodsugarrbs, datetime=datetime1)

        
        # doctoruserdata = vitals_data.objects.get(patient_id = pd)
        # doctoruserdata.bodytemperature = bodytemperature
        # doctoruserdata.pulserate = pulserate
        # doctoruserdata.respiratoryrate = respiratoryrate
        # doctoruserdata.bp = bp
        # doctoruserdata.spo2 = spo2
        # doctoruserdata.weight = weight
        # doctoruserdata.bloodsugarfbs = bloodsugarfbs
        # doctoruserdata.bloodsugarrbs = bloodsugarrbs
        # doctoruserdata.datetime = datetime1

        v_data.save()
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

def mobilabtest(request):
    import requests
    if request.method == "POST":
        userid = request.POST['userid']
        albumin = request.POST.get('albumin')
        glucose = request.POST.get('glucose')
        triglyceride = request.POST.get('triglyceride')
        cholesterol = request.POST.get('cholesterol')
        ldl = request.POST.get('ldl')
        total_protein = request.POST.get('total_protein')
        uric_acid = request.POST.get('uric_acid')
        haemoglobin = request.POST.get('haemoglobin')
        creatinine = request.POST.get('creatinine')
        bili = request.POST.get('bili')

        print(userid, albumin, glucose, triglyceride, cholesterol, ldl, total_protein, uric_acid, haemoglobin, creatinine, bili)
        
        test_values = [albumin, glucose, triglyceride, cholesterol, ldl, total_protein, uric_acid, haemoglobin, creatinine, bili]

        test_id = {
            'Albumin' : 1, 'Glucose' : 3, 'Triglyceride' : 7, 'Cholesterol' : 8, 'LDL' : 10, 
            'Total_Protein' : 12, 'Uric_Acid' : 16, 'Haemoglobin' : 17, 'Creatinine' : 20, 'Bilirubin_Total' : 23}
        
        all_tests = ['Albumin', 'Glucose',  'Triglyceride', 'Cholesterol', 'LDL', 'Total_Protein', 'Uric_Acid', 'Haemoglobin', 'Creatinine', 'Bilirubin_Total']
        test_to_perform = []
        for test in range(len(all_tests)):
            if test_values[test] == 'Yes' :
            # if int(test_values[test]) == 1:
                test_to_perform.append(all_tests[test])
        print('test_to_perform :', test_to_perform)

        test_to_perform_id = []
        for test1 in test_to_perform:
            test_to_perform_id.append(test_id[test1])
        print('test_to_perform_id :', test_to_perform_id)

        final_list = []
        # final_dict =  dict(zip(test_to_perform, test_perform_id))
        for test in range(len(test_to_perform)):
           new_dict = {"test_name" : test_to_perform[test], "test_id" : test_to_perform_id[test]}
           final_list.append(new_dict)

        print('final_list :', final_list)

        data = Patient_data.objects.get(patient_id = userid)
        fullname = data.fullname
        age = data.age
        gender = data.gender
        print(fullname, age, gender)

        if int(gender) == 0:
            new_gender = "Male"
        else:
            new_gender = "Female" 


        booktest_url  = 'https://emobilab.in/api-vendor/bookTest.php'

        param = {}
        param["secret_key"] = "a99H-FUjS-9CrG-hMY5"
        param["fullname"] = fullname
        param["age"] = age
        param["tests"] = final_list
        param["gender"] = new_gender
        param["phone"] = 1234567809
        # param = {
        #     "secret_key = "a99H-FUjS-9CrG-hMY5"" : "a99H-FUjS-9CrG-hMY5",
        #     "fullname" : fullname,
        #     "age" : age,
        #     "gender" : gender,
        #     "tests" : final_list
        # }
        print(param)

        response = requests.post(booktest_url, json=param)
        bookid = response.json()
        # print(response.json())
        id_booked = bookid["bookingID"]
        print('id_booked :', id_booked)
        return render(request, 'doctor/mobilabsuccess.html', {'bookingid' : id_booked})

    return render(request, 'doctor/mobilabtest.html')

def mobilabsuccess(request):
    return render(request, 'doctor/mobilabsuccess.html')

def dhearthealthpredictor(request):
    if request.method == "POST":
        user_id = request.POST['userid']

        heart_modal_path = os.path.join(settings.BASE_DIR, 'User', 'prediction_model', 'heart_disease_model.sav')
        print(heart_modal_path)
        heart_model = pickle.load(open(heart_modal_path, 'rb'))
        print('success')

        global p_id
        p_id = user_id
        data = Patient_data.objects.get(patient_id = user_id)

        heart_data = []
        heart_data.append(int(data.age))
        heart_data.append(int(data.gender))
        heart_data.append(int(data.chestpaintype))
        heart_data.append(int(data.bloodpressure))
        heart_data.append(int(data.prediabetic))
        heart_data.append(int(data.cholestrol))
        # heart_data.append(int(data.heartrate))
        heart_data.append(int(data.cholestrol))

        input_data_as_np_array = np.asarray(heart_data)
        input_reshaped_data = input_data_as_np_array.reshape(1, -1)
        print(1)
        prediction = heart_model.predict(input_reshaped_data)
        print(2)
        # global global_prediction
        heart_result = prediction[0]
        print(3)
        if heart_result == 0:
            result = 'No worries!! Your heart is safe'
            color = 'green'
            print(4)
            context = {
                'result' : result,
                'color' : color 
            }
            return render(request, 'doctor/dhearthealthresult.html', context=context)
        else:
            result = 'Alert!! Your heart is at risk'
            color = 'red'
            context = {
                'result' : result,
                'color' : color 
            }
            print(5)
        return render(request, 'doctor/dhearthealthresult.html', context=context)
    return render(request, 'doctor/dhearthealthpredictor.html')

def dbloodglucosepredictor(request):
    if request.method == "POST":
        user_id = request.POST['userid']

        diabetes_modal_path = os.path.join(settings.BASE_DIR, 'User', 'prediction_model', 'diabetes_model.sav')
        print(diabetes_modal_path)
        diabetes_model = pickle.load(open(diabetes_modal_path, 'rb'))
        print('success')

        data = Patient_data.objects.get(patient_id = user_id)

        diabetes_data = []
        diabetes_data.append(int(data.age))
        diabetes_data.append(int(data.glucosevalue))
        diabetes_data.append(int(data.bloodpressure))
        diabetes_data.append(int(data.insulinvalue))
        diabetes_data.append(int(data.bmi))
        diabetes_data.append(int(data.dpf))
        # diabetes_data.append(int(data.cholestrol))

        input_data_as_np_array = np.asarray(diabetes_data)
        input_reshaped_data = input_data_as_np_array.reshape(1, -1)
        print(1)
        prediction = diabetes_model.predict(input_reshaped_data)
        print(2)
        # global global_prediction
        diabetes_result = prediction[0]
        print(3)
        if diabetes_result == 0:
            result = 'No worries!! You are Safe from diabetic'
            color = 'green'
            print(4)
            context = {
                'result' : result,
                'color' : color 
            }
            return render(request, 'doctor/dbloodglucoseresult.html', context=context)
        else:
            result = 'Alert!! You are diabetic. Recommended: DR Test'
            color = 'red'
            context = {
                'result' : result,
                'color' : color 
            }
            result = 'Alert!! You are diabetic. Recommended: DR Test'
            print(5)
            return render(request, 'doctor/dbloodglucoseresult.html', context=context)
    return render(request, 'doctor/dbloodglucosepredictor.html')

def iframeview(request):
    path_obj =  Patient_data.objects.get(patient_id=7)

    # path = f'{path_obj.esio_patient_name}/{path_obj.esio_folder_name}' for 2d_path
    path = f'{path_obj.esio_patient_name}'
    return render(request, 'doctor/iframetest.html', {'path' : path})

def doctorlogout(request):
    logout(request)
    return redirect('CharakHome')