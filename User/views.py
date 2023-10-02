from django.shortcuts import render, redirect
from django.http import HttpResponse
from Manager.models import Patient_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from datetime import datetime, timedelta
from .models import watch_data, medication_data, exercise_data, eating_habits_data, todays_feel_data, health_condition_data, vitals_data, eating_habits_other, prescription_data, iglu_data
import matplotlib.pyplot as plt
from django.conf import settings
import pickle
import os
import plotly.express as px
import io
import mpld3
from django.db.models import Q
from cryptography.fernet import Fernet ## library used for encryption and decryption
import numpy as np
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# secret_key = Fernet.generate_key()
# cipher_suite = Fernet(secret_key)

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def userlogin(request):
    if request.method == "POST":
        
        # user_data = Patient_data.objects.get(all)
        user_email = request.POST['userloginemail']
        user_password = request.POST['userloginpassword']
        print(user_email)

        # authenticate the user
        user = authenticate(username=user_email, password=user_password)

        if user is not None:
            print('user authenticated')
            login(request, user)
            # messages.success(request, "Successfully logged in")

            # enc_user_email = (user_email).encode('utf-8')
            # hashed_email = cipher_suite.encrypt(enc_user_email)
            # print(hashed_email)

            data = Patient_data(email = user_email)
            # data = Patient_data(email = user_email)

            user_data = Patient_data.objects.get(email = user_email)
            print(user_data.email)
            # user_data = Patient_data.objects.get(email = user_email)
            global patient_id
            patient_id = user_data.patient_id
            print('patient_id :', patient_id)
            user_watch_date = []
            user_watch_steps = []

            current_date = datetime.now() - timedelta(days=30)
            # user_watch_data = watch_data.objects.filter(patient_id=patient_id, date__month=current_date.month, date__year=current_date.year)

            # Extract the current month and year from the current date
            current_month = current_date.month
            current_year = current_date.year

            # Assuming patient_id is the variable containing the patient's ID
            user_watch_data = watch_data.objects.filter(patient_id=patient_id, date__month=current_month, date__year=current_year)
            print(user_watch_data)
            global data1_date, data1_steps, data2_date, data2_steps, data3_date, data3_steps, total_steps, avg_steps
            data1_steps = []
            data1_date = []
            data2_steps = []
            data2_date = []
            data3_steps = []
            data3_date = []
            total_steps = []
            for data in user_watch_data:
                user_watch_date.append(data.date)
                user_watch_steps.append(data.steps)
                if data.date.day < 11:
                    data1_steps.append(data.steps)
                    data1_date.append(data.date)
                elif data.date.day > 10 and data.date.day < 21:
                    data2_date.append(data.date)
                    data2_steps.append(data.steps)
                else:
                    data3_date.append(data.date)
                    data3_steps.append(data.steps)
            print('data1_steps :', data1_steps)
            print('data1_date :', data1_date)
            print('data2_steps :', data2_steps)
            print('data2_date :', data2_date)
            print('data3_steps :', data3_steps)
            print('data3_date :', data3_date)

            total_steps = data1_steps + data2_steps + data3_steps
            steps = 0
            days = 1
            for step in total_steps:
                if step != 0:
                    steps = steps+ int(step)
                    days = days + 1
            avg_steps = int(steps//days)
            print('avg_steps :', avg_steps)

            # total_steps = total_steps.extend(data1_steps).extend(data2_steps).extend(data3_steps)

            print('total_steps :', total_steps)
            print(user_watch_date)
            print(user_watch_steps)

            # <============ for heart points ==================>
            global heart_point_1_5, heart_point_6_10, heart_point_11_15, heart_point_16_20, heart_point_21_25, heart_point_26_30, total_heart_points, avg_hp
           
            heart_point_1_5 = int(0)
            heart_point_6_10 = int(0)
            heart_point_11_15 = int(0)
            heart_point_16_20 = int(0)
            heart_point_21_25 = int(0)
            heart_point_26_30 = int(0)
            total_heart_points = []
            for data in user_watch_data:
                if data.date.day > 0 and data.date.day <= 5:
                    heart_point_1_5 = heart_point_1_5 + int(data.heart_minutes)
                    # heart_point_1_5.append(data.heart_minutes)
                if data.date.day > 5 and data.date.day < 11:
                    heart_point_6_10 = heart_point_6_10 + int(data.heart_minutes)
                    # heart_point_6_10.append(data.heart_minutes)
                if data.date.day > 10 and data.date.day < 16:
                    heart_point_11_15 = heart_point_11_15 + int(data.heart_minutes)
                    # heart_point_11_15.append(data.heart_minutes)
                if data.date.day > 15 and data.date.day < 21:
                    heart_point_16_20 = heart_point_16_20 + int(data.heart_minutes)
                    # heart_point_16_20.append(data.heart_minutes)
                if data.date.day > 20 and data.date.day < 26:
                    heart_point_21_25 = heart_point_21_25 + int(data.heart_minutes)
                    # heart_point_21_25.append(data.heart_minutes)
                if data.date.day > 25 and data.date.day <= 30:
                    heart_point_26_30 = heart_point_26_30 + int(data.heart_minutes)
                    # heart_point_26_30.append(data.heart_minutes)

            total_heart_points = heart_point_1_5 + heart_point_6_10 + heart_point_11_15 + heart_point_16_20 + heart_point_21_25 + heart_point_26_30
            
            print('total_heart_points :' , total_heart_points)

            avg_hp = int(total_heart_points//days)
            print('avg_hp :', avg_hp)
            
            # <============ for Calories Burnt ==================>
            global avg_calburnt_1_5, avg_calburnt_6_10, avg_calburnt_11_15, avg_calburnt_16_20, avg_calburnt_21_25, avg_calburnt_26_30, total_calories_burnt, avg_calburnt
           
            # avg_calburnt_1_5 = int(0)
            # avg_calburnt_6_10 = int(0)
            # avg_calburnt_11_15 = int(0)
            # avg_calburnt_16_20 = int(0)
            # avg_calburnt_21_25 = int(0)
            # avg_calburnt_26_30 = int(0)
            calburnt_1_5 = int(0)
            calburnt_6_10 = int(0)
            calburnt_11_15 = int(0)
            calburnt_16_20 = int(0)
            calburnt_21_25 = int(0)
            calburnt_26_30 = int(0)
            for data in user_watch_data:
                if data.date.day > 0 and data.date.day <= 5:
                    calburnt_1_5 = calburnt_1_5 + float(data.calories_burnt)
                    # heart_point_1_5.append(data.heart_minutes)
                if data.date.day > 5 and data.date.day < 11:
                    calburnt_6_10 = calburnt_6_10 + float(data.calories_burnt)
                    # heart_point_6_10.append(data.heart_minutes)
                if data.date.day > 10 and data.date.day < 16:
                    calburnt_11_15 = calburnt_11_15 + float(data.calories_burnt)
                    # heart_point_11_15.append(data.heart_minutes)
                if data.date.day > 15 and data.date.day < 21:
                    calburnt_16_20 = calburnt_16_20 + float(data.calories_burnt)
                    # heart_point_16_20.append(data.heart_minutes)
                if data.date.day > 20 and data.date.day < 26:
                    calburnt_21_25 = calburnt_21_25 + float(data.calories_burnt)
                    # heart_point_21_25.append(data.heart_minutes)
                if data.date.day > 25 and data.date.day <= 30:
                    calburnt_26_30 = calburnt_26_30 + float(data.calories_burnt)
                    # heart_point_26_30.append(data.heart_minutes)
            
            avg_calburnt_1_5 = int(calburnt_1_5 // 5)
            avg_calburnt_6_10 = int(calburnt_6_10 // 5)
            avg_calburnt_11_15 = int(calburnt_11_15 // 5)
            avg_calburnt_16_20 = int(calburnt_16_20 // 5)
            avg_calburnt_21_25 = int(calburnt_21_25 // 5)
            avg_calburnt_26_30 = int(calburnt_26_30 // 5)

            total_calories_burnt = calburnt_1_5 + calburnt_6_10 + calburnt_11_15 + calburnt_16_20 + calburnt_21_25 + calburnt_26_30
            avg_calburnt = int(total_calories_burnt//days)
            
            global pulserate, respiratory, bp, weight, fbs, rbs
            try:
                last_pd = Patient_data.objects.get(patient_id=patient_id)
                last_entry = vitals_data.objects.filter(patient_id=last_pd).latest('datetime')
                pulserate = last_entry.pulserate
                respiratory = last_entry.respiratoryrate
                bp = last_entry.bp
                weight = last_entry.weight
                fbs = last_entry.bloodsugarfbs
                rbs = last_entry.bloodsugarrbs
            except:
                pulserate = 0
                respiratory = 0
                bp = 0
                weight = 0
                fbs = 0
                rbs = 0
            # last_entry = vitals_data.objects.latest('datetime')
            

            print('pulserate :', pulserate, 'respiratory :', respiratory,  'bp :', bp, 'weight :', weight, 'fbs :', fbs, 'rbs :', rbs)

            print(avg_calburnt_1_5, avg_calburnt_6_10, avg_calburnt_11_15, avg_calburnt_16_20, avg_calburnt_21_25, avg_calburnt_26_30)
            # Data for the bar graph
            date_on = user_watch_date
            # categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
            step_count = user_watch_steps

            # Create a bar graph
            # plt.bar(date_on, step_count, width=0.2)
            # plt.xlabel('Date')
            # plt.ylabel('Toatl Step Count')
            # plt.title('Bar Graph Example')

            # Save the graph in the same directory as the script
            # app_static_dir = os.path.join(settings.STATICFILES_DIRS[3], 'graphs')
            # image_path = os.path.join(app_static_dir, 'bar_graph.png')
            # plt.savefig(image_path)

            # Close the Matplotlib plot to prevent displaying it in the console
            # plt.close()

            return render( request, 'user/index_na.html', {'user_data' : user_data, 'data1_date' : data1_date, 'data1_steps' : data1_steps, 'data2_date' : data2_date, 'data2_steps' : data2_steps, 'data3_date' : data3_date, 'data3_steps' : data3_steps, 
                    'heart_point_1_5' : heart_point_1_5, 'heart_point_6_10' : heart_point_6_10, 'heart_point_11_15' : heart_point_11_15, 'heart_point_16_20' : heart_point_16_20, 'heart_point_21_25': heart_point_21_25, 'heart_point_26_30' : heart_point_26_30, 
                    'avg_calburnt_1_5' : avg_calburnt_1_5, 'avg_calburnt_6_10' : avg_calburnt_6_10, 'avg_calburnt_11_15' :avg_calburnt_11_15, 'avg_calburnt_16_20' : avg_calburnt_16_20, 'avg_calburnt_21_25' : avg_calburnt_21_25, 'avg_calburnt_26_30' : avg_calburnt_26_30,
                     'avg_steps' : avg_steps, 'avg_hp' : avg_hp, 'avg_calburnt':avg_calburnt, 'pulserate':pulserate, 'respiratory':respiratory, 'bp':bp, 'weight':weight, 'fbs':fbs, 'rbs':rbs } )
            # return render( request, 'user/index_na.html', {'user_data' : user_data, 'user_watch_data' : user_watch_data} )
            # return redirect('ManagerHome')
        else:
            # messages.error(request, "Invalied Credentilas")
            # return redirect("#")
            return redirect("UserLogin")

        # user_data = Patient_data.objects.get(email = user_email)
        # global patient_id
        # patient_id = user_data.patient_id
        # # print(user_data.fullname)
        # return render( request, 'user/index_na.html', {'user_data' : user_data} )
    # return render(request, 'user/userlogin.html')

# def userhome(request):
#     user_data = Patient_data.objects.get(patient_id=patient_id)
#     return render(request, 'user/index_na.html',  {'patient_id' : patient_id, 'user_data' : user_data, 'data1_date' : data1_date, 'data1_steps' : data1_steps, 'data2_date' : data2_date, 'data2_steps' : data2_steps, 'data3_date' : data3_date, 'data3_steps' : data3_steps, 
#         'heart_point_1_5' : heart_point_1_5, 'heart_point_6_10' : heart_point_6_10, 'heart_point_11_15' : heart_point_11_15, 'heart_point_16_20' : heart_point_16_20, 'heart_point_21_25': heart_point_21_25, 'heart_point_26_30' : heart_point_26_30, 
#         'avg_calburnt_1_5' : avg_calburnt_1_5, 'avg_calburnt_6_10' : avg_calburnt_6_10, 'avg_calburnt_11_15' :avg_calburnt_11_15, 'avg_calburnt_16_20' : avg_calburnt_16_20, 'avg_calburnt_21_25' : avg_calburnt_21_25, 'avg_calburnt_26_30' : avg_calburnt_26_30, 
#         'avg_steps' : avg_steps, 'avg_hp' : avg_hp, 'avg_calburnt':avg_calburnt, 'pulserate':pulserate, 'respiratory':respiratory, 'bp':bp, 'weight':weight, 'fbs':fbs, 'rbs':rbs   })
#     # return render(request, 'user/userhome.html')

def accesshealthdata(request):
    if request.method == "POST":
        return redirect('HealthData')
    return render(request, 'user/accesshealthdata.html')

def healthdata(request):
    print(patient_id)
    id  = patient_id
    user_hdata = Patient_data.objects.get(patient_id=id)
    user_vital_latest = vitals_data.objects.latest('datetime')
    user_vital = vitals_data.objects.filter(patient_id=user_hdata)
    user_exercises = exercise_data.objects.filter(patient_id=user_hdata)
    user_medications = medication_data.objects.filter(patient_id=user_hdata)
    user_eating = eating_habits_other.objects.filter(patient_id=user_hdata)
    user_health_condition = health_condition_data.objects.filter(patient_id=user_hdata)
    user_today = todays_feel_data.objects.filter(patient_id=user_hdata)

    # print(user_hdata.report.url)
    # print(user_hdata.xray.url)

    context = {
        'user_hdata' : user_hdata,
        'user_vital_latest' : user_vital_latest,
        'user_vital' : user_vital,
        'user_exercises' : user_exercises,
        'user_medications' : user_medications,
        'user_eating' : user_eating,
        'user_health_condition' : user_health_condition,
        'user_today' : user_today
    }
    return render(request, 'user/healthdata.html', context=context)
    # return render(request, 'user/healthdata.html', {'user_hdata' : user_hdata})

def editvitalsings(request):
    if request.method == "POST":
        print('12358')
        # userid = request.POST['userid']
        # chestpaintype = request.POST['chestpaintype']
        # glucose = request.POST['glucose']
        # heartrate = request.POST['heartrate']
        # bloodpressure = request.POST['bloodpressure']
        # insulin = request.POST['insulin']
        # bmi = request.POST['bmi']
        # prediabetic = request.POST['prediabetic']
        # dpf = request.POST['dpf']
        # cholestrol = request.POST['cholestrol']
        # dailyexercisehr = request.POST['dailyexercisehr']
        # sleepinghabit = request.POST['sleepinghabit']
        # brushinghabit = request.POST['brushinghabit']

        # print(userid, bmi, bloodpressure, glucose)
        # updatedata = Patient_data.objects.get(patient_id = userid)
        # updatedata.chestpaintype = chestpaintype
        # updatedata.glucosevalue = glucose
        # updatedata.bloodpressure = bloodpressure
        # updatedata.insulinvalue = insulin
        # updatedata.bmi = bmi
        # updatedata.prediabetic = prediabetic
        # updatedata.dpf = dpf
        # updatedata.cholestrol = cholestrol
        # updatedata.dailyexercise = dailyexercisehr
        # updatedata.brushinghabits = brushinghabit
        # updatedata.sleepinghabits = sleepinghabit
        # updatedata.save()
        # print('updatedata :', updatedata)
        
        # <========= New edit health data fields =========>
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

        pd = Patient_data.objects.get(patient_id = patient_id)
        v_data = vitals_data(patient_id=pd, bodytemperature=bodytemperature, pulserate=pulserate, respiratoryrate=respiratoryrate, bp=bp, spo2=spo2, weight=weight, bloodsugarfbs=bloodsugarfbs, bloodsugarrbs=bloodsugarrbs, datetime=datetime1)
        v_data.save()

        return redirect('EditHealthSuccess')
    
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/editvitaldata.html', {'user_data':user_data})

def uploadprescription(request):
    if request.method == "POST":
        user_id = request.POST['userid']
        doctorname = request.POST['doctorname']
        datetime1 = request.POST['datetime1']
        pdf = request.FILES.get('pdf')
        # pdf = request.FILES.get('pdf')

        print(user_id, pdf)

        pd_obj2 = Patient_data.objects.get(patient_id = user_id)
        print('database :', pd_obj2.pdf)
        pd_obj2.pdf = pdf
        pd_obj2.save()

        pres_obj = prescription_data(patient_id=pd_obj2, doctorname=doctorname, prescription=pdf, datetime=datetime1)
        pres_obj.save()

        data = Patient_data.objects.get(patient_id=user_id)

        print('pdf :', data.pdf)
        print(type(data.pdf))
        return render(request, 'user/uploadsuccess.html') 
    return render(request, 'user/uploadprescription.html')

def viewprescription(request):
    obj_vp = Patient_data.objects.get(patient_id=patient_id)
    view_obj = prescription_data.objects.filter(patient_id=obj_vp)

    return render(request, 'user/viewprescription.html', {'view_data' : view_obj})

def edithealthsuccess(request):
    if request.method == "POST":
        '''userid, chestpaintype, glucose, heartrate, bloodpressure, insulin, bmi, prediabetic, dpf, cholestrol, dailyexercisehr, sleepinghabit, brushinghabit '''

        return redirect( "{% url 'PatientHome' %}")
    return render(request, 'user/edithealthsuccess.html')

def editeatinghabits(request):
    if request.method == "POST":
        # breakfast
        bjeerarice = request.POST.get('bjeerarice', 'na')
        bbiryani = request.POST.get('bbiryani', 'na')
        bdal = request.POST.get('bdal', 'na')
        btikka = request.POST.get('btikka', 'na')
        bbchicken = request.POST.get('bbchicken', 'na')
        bchole = request.POST.get('bchole', 'na')
        baloogobi = request.POST.get('baloogobi', 'na')
        bmixveg = request.POST.get('bmixveg', 'na')
        bchickencurry = request.POST.get('bchickencurry', 'na')

        # lunch
        lbutterchicken = request.POST.get('lbutterchicken', 'na')
        lchole = request.POST.get('lchole', 'na')
        laloogobi = request.POST.get('laloogobi', 'na')
        lupma = request.POST.get('lupma', 'na')
        lpoha = request.POST.get('lpoha', 'na')
        lidli = request.POST.get('lidli', 'na')
        ldosa = request.POST.get('ldosa', 'na')
        lalooparatha = request.POST.get('lalooparatha', 'na')
        lpoori = request.POST.get('lpoori', 'na')
        lbhature = request.POST.get('lbhature', 'na')
        lmeduvada = request.POST.get('lmeduvada', 'na')
        lsamosa = request.POST.get('lsamosa', 'na')

        # dinner
        dtikka = request.POST.get('dtikka','na')
        dbutterchicken = request.POST.get('dbutterchecken','na')
        dchole = request.POST.get('dchole','na')
        daloogobi = request.POST.get('daloogobi','na')
        dmixveg = request.POST.get('dmixveg','na')
        dupma = request.POST.get('dupma','na')
        dpoha = request.POST.get('dpoha','na')
        didli = request.POST.get('didli','na')
        dbhature = request.POST.get('dbhature','na')
        dmeduvada = request.POST.get('dmeduvada','na')
        dsamosa = request.POST.get('dsamosa','na')
        ddosa = request.POST.get('ddosa','na')
        dpoori = request.POST.get('dpoori','na')

        datetime1 = request.POST['datetime1']

        eat_pat = Patient_data.objects.get(patient_id=patient_id)

        eat_obj = eating_habits_data(patient_id=eat_pat, datetime=datetime1, bjeerarice=bjeerarice, bbiryani=bbiryani, bbchicken=bbchicken, bdal=bdal, btikka=btikka, bchole=bchole, baloogobi=baloogobi, bmixveg=bmixveg, bchickencurry=bchickencurry,
                                  lbutterchicken=lbutterchicken, lchole=lchole, laloogobi=laloogobi, lupma=lupma, lpoha=lpoha, ldosa=ldosa, lidli=lidli, lalooparatha=lalooparatha, lpoori=lpoori, lmeduvada=lmeduvada, lbhature=lbhature, lsamosa=lsamosa,
                                  dtikka=dtikka, dbutterchecken=dbutterchicken, dchole=dchole, daloogobi=daloogobi, dmixveg=dmixveg, dupma=dupma, dpoha=dpoha, didli=didli, dbhature=dbhature, dmeduvada=dmeduvada, dsamosa=dsamosa, ddosa=ddosa, dpoori=dpoori) 
        eat_obj.save()   

        return redirect('EditHealthSuccess')

    return render(request, 'user/editeatinghabits.html')

def editeatinghabitsother(request):
    if request.method == "POST":
        datetime1 = request.POST["datetime1"]
        breakfast = request.POST["breakfast"]
        lunch = request.POST["lunch"]
        high_tea = request.POST['high_tea']
        dinner = request.POST["dinner"]

        other_pd = Patient_data.objects.get(patient_id=patient_id)

        other_obj = eating_habits_other(patient_id=other_pd, breakfast=breakfast, lunch=lunch, high_tea=high_tea, dinner=dinner, datetime=datetime1)
        other_obj.save()

        return render(request, 'user/edithealthsuccess.html')
    return render(request, 'user/editeatinghabitsother.html')

def addcredentials(request):
    if request.method == "POST":
        client_id = request.POST['googleclientid']
        client_secretkey = request.POST['googleclientsecretkey']

        obj = Patient_data.objects.get(patient_id = patient_id)
        obj.google_client_id = client_id
        obj.google_secret_key = client_secretkey
        obj.save() 
        return render(request, 'user/successconnect.html')
    return render(request, 'user/addcredentials.html')

def connectsmartphone(request):
    from oauthlib.oauth2 import WebApplicationClient
    from requests_oauthlib import OAuth2Session
    from datetime import datetime
    import os
    # Define the Google Fit API endpoints
    authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
    token_url = 'https://accounts.google.com/o/oauth2/token'

    # if request.method == "POST":
    global googleclientid, googlesecretkey, userredirecturi
    # googleclientid = request.POST['googleclientid']
    # googlesecretkey = request.POST['googleclientsecretkey']
    # userredirecturi = request.POST['userredirecturi']
    obj = Patient_data.objects.get(patient_id = patient_id)
    googleclientid = obj.google_client_id
    googlesecretkey = obj.google_secret_key

    # userid = request.POST['userid']
    print('googleclientid', googleclientid)
    print('googlesecretkey', googlesecretkey)
    # print('userredirecturi', userredirecturi)

    # Create an OAuth2Session with your client ID and specify the scope and redirect_uri here
    global oauth
    oauth = OAuth2Session(
    client_id=googleclientid,
    redirect_uri= 'https://127.0.0.1:8000/user/successconnect',
    scope=['https://www.googleapis.com/auth/fitness.activity.read', 'https://www.googleapis.com/auth/fitness.heart_rate.read', 'https://www.googleapis.com/auth/fitness.location.read', 'https://www.googleapis.com/auth/fitness.body.read', 'https://www.googleapis.com/auth/fitness.nutrition.read', 'https://www.googleapis.com/auth/fitness.blood_pressure.read', 'https://www.googleapis.com/auth/fitness.blood_glucose.read', 'https://www.googleapis.com/auth/fitness.oxygen_saturation.read', 'https://www.googleapis.com/auth/fitness.body_temperature.read', 'https://www.googleapis.com/auth/fitness.reproductive_health.read' ]
    )

    # Generate the authorization URL
    authorization_url, state = oauth.authorization_url(
        authorization_base_url)
    print('authorization_url :', authorization_url )
        
    # Paths to your SSL certificate and private key
    # cert_file = 'cert.pem'
    # key_file = 'key.pem'
    # print(authorization_url)
    return redirect(authorization_url)

    # return render(request, 'user/connectsmartphone.html')

def successconnect(request):
    from oauthlib.oauth2 import WebApplicationClient
    from requests_oauthlib import OAuth2Session
    from datetime import datetime
    import requests
    token_url = 'https://accounts.google.com/o/oauth2/token'
    
    # Define your start and end dates
    start_date = datetime(2023, 9, 1)
    end_date = datetime.now()
    # end_date = datetime(2023, 9, 24)

    # Convert the dates to Unix timestamps in milliseconds
    start_timestamp = int(start_date.timestamp()) * 1000
    end_timestamp = int(end_date.timestamp()) * 1000

    # Handle the authorization response
    authorization_response = request.build_absolute_uri()
    # authorization_response = request.url
    print('authorization_response :', authorization_response)
    print('token_url :', token_url)
    token = oauth.fetch_token(
        token_url,
        authorization_response=authorization_response,
        client_id= googleclientid,
        client_secret= googlesecretkey
    )
    print('token :', token)
    # API endpoint for retrieving fitness data

    api_url = 'https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate'
    # api_url = 'https://www.googleapis.com/fitness/v1/users/me/dataSources'

    # Set up your request headers with the access token
    headers = {
        'Authorization': f'Bearer {token["access_token"]}',
        "Content-Type": "application/json"
    }

    # =============== Api request for Step Count ==============

    # parameters for stepcount
    params_stepcount = {
        'aggregateBy': [{ 
                    'dataTypeName': 'com.google.step_count.delta',
                    'dataSourceId':
                        'derived:com.google.step_count.delta:com.google.android.gms:estimated_steps'
                    }],
        'bucketByTime': { 'durationMillis': 86400000 },
        'startTimeMillis': str(start_timestamp),
        'endTimeMillis': str(end_timestamp),
    }

    # Make the API request for step count
    response = requests.post(api_url, headers=headers, json=params_stepcount)
    if response.status_code == 200:
        steps = response.json()  
        print(steps)
        length = len(steps['bucket'])
        step_list = []
        for i in range(length):
            if len(steps['bucket'][i]['dataset'][0]['point']) != 0:
                step_list.append(steps['bucket'][i]['dataset'][0]['point'][0]['value'][0]['intVal'])
            else:
                step_list.append(0)

        date_val_dict = {}

        current_date = start_date
        for day in range(len(step_list)):
            # formatted_date = current_date.strftime("%d-%m-%Y")
            formatted_date = current_date.strftime("%Y-%m-%d")
            value = step_list[day]
            date_val_dict[formatted_date] = value
            current_date += timedelta(days=1)
        print('date_val_dict :', date_val_dict)
        # data_obj = watch_data.objects.get(patient_id = patient_id)
        for date, steps in date_val_dict.items():
            try:
                data_obj = watch_data.objects.get(date = date, patient_id=patient_id)
                data_obj.steps = steps
                data_obj.save()
            except:
                data_obj = watch_data(date = date, patient_id = patient_id, steps=steps)
                data_obj.save() 
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  

    # =============== Api request for Heart Rate ==============

    params_heartrate = {
        "aggregateBy": [{ 
                            "dataTypeName": "com.google.heart_rate.bpm",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }
    
    response = requests.post(api_url, headers=headers, json=params_heartrate)
    if response.status_code == 200:
        heartrate = response.json()  # If the response contains JSON data
        # print('heartrate :', heartrate)
        length_hr = len(heartrate['bucket'])
        print('length of heartrate bucket :', length_hr)
        
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  

    # =============== Api request for Distance ==============
    # parameters for distance
    params_distance = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.distance.delta:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.distance.delta",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_distance)
    if response.status_code == 200:
        distance = response.json()  
        # print('distance :', distance)
        length = len(distance['bucket'])
        print('length of distance bucket :', distance)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text) 

    # =============== Api request for calories expended ==============
    params_calories = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.calories.expended:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.calories.expended",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_calories)
    if response.status_code == 200:
        calories = response.json() 
        print('calories :', calories) 
        length_calories = len(calories['bucket'])
        print('length of calories bucket :', length_calories)
        calories_list = []

        for i in range(length_calories):
            if len(calories['bucket'][i]['dataset'][0]['point']) != 0:
                calories_list.append(calories['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal'])
            else:
                calories_list.append(0)

        date_cal_dict = {}

        current_date = start_date
        for day in range(length_calories):
            formatted_date = current_date.strftime("%Y-%m-%d")
            cal_value = calories_list[day]
            date_cal_dict[formatted_date] = cal_value
            current_date += timedelta(days=1)
        print('date_cal_dict :', date_cal_dict)
        # data_obj = watch_data.objects.get(patient_id = patient_id)
        for date, cals in date_cal_dict.items():
            # cal_obj = watch_data(patient_id = patient_id, date=date, calories_burnt = cals )
            # cal_obj.save()
            try:
                cal_obj = watch_data.objects.get(date = date, patient_id=patient_id)
                cal_obj.calories_burnt = cals
                cal_obj.save()
            except:
                cal_obj = watch_data(date = date, patient_id = patient_id, calories_burnt=cals)
                cal_obj.save() 

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text) 

    # =============== Api request for speed ==============
    params_calories = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.speed.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.speed",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_calories)
    if response.status_code == 200:
        speed = response.json()  
        length_speed = len(speed['bucket'])
        print('length of speed bucket :', length_speed)
        speed_list = []
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text) 


    # =============== Api request for activity segment ==============
    params_activity = {
        "aggregateBy": [{ 
                            "dataSourceId": 'derived:com.google.activity.segment:com.google.android.gms:merge_activity_segments',
                            "dataTypeName": "com.google.activity.segment",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_activity)
    if response.status_code == 200:
        activity = response.json()  
        # print('activity :', activity)
        length_activity = len(activity['bucket'])
        print('length of activity bucket :', length_activity)
        activity_list = []
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  

    # =============== Api request for weight ==============
    # parameters for weight
    params_weight = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.weight.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.weight",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_weight)
    if response.status_code == 200:
        weight = response.json()  
        # print('weight :', weight)
        length_weight = len(weight['bucket'])
        print('length of weight bucket :', length_weight)
        weight_list = []
    else:
        print(f"Request for weight failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Blood Pressure ==============
    params_bloodpressure = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.blood_pressure.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.blood_pressure",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_bloodpressure)
    if response.status_code == 200:
        bloodpressure = response.json() 
        # print('bloodpressure :', bloodpressure)
        length_bloodpressure = len(bloodpressure['bucket'])
        print('length of bloodpressure bucket :', length_bloodpressure)
        activity_list = []
    else:
        print(f"Request for bloodpressure failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Blood Glucose ==============
    params_bloodglucose = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.blood_pressure.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.blood_glucose",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_bloodglucose)
    if response.status_code == 200:
        bloodglucose = response.json()  
        # print('bloodglucose :', bloodglucose)
        length_bloodglucose = len(bloodglucose['bucket'])
        print('length of bloodglucose bucket :', length_bloodglucose)
        bloodglucose_list = []
    else:
        print(f"Request for bloodglucose failed with status code: {response.status_code}")
        print(response.text)  

    # =============== Api request for Oxygen Saturation ==============
    params_oxygensaturation = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.blood_pressure.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.oxygen_saturation",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_oxygensaturation)
    if response.status_code == 200:
        oxygensaturation = response.json()  
        # print('oxygensaturation :', oxygensaturation)
        length_oxygensaturation = len(oxygensaturation['bucket'])
        print('length of oxygensaturation bucket :', length_oxygensaturation)
        oxygensaturation_list = []
    else:
        print(f"Request for oxygensaturation failed with status code: {response.status_code}")
        print(response.text) 

    # =============== Api request for Body Temperature ==============
    params_temperature = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.blood_pressure.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.body.temperature",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_temperature)
    if response.status_code == 200:
        temperature = response.json()  
        # print('temperature :', temperature)
        length_temperature = len(temperature['bucket'])
        print('length of temperature bucket :', length_temperature)
        temperature_list = []
    else:
        print(f"Request for temperature failed with status code: {response.status_code}")
        print(response.text) 

    # =============== Api request for Heart Minutes ==============
    params_heartminutes = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.heart_minutes.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.heart_minutes",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_heartminutes)
    if response.status_code == 200:
        heartminutes = response.json() 
        print('heartminutes :', heartminutes)
        length_heartminutes = len(heartminutes['bucket'])
        print('length of heartminutes bucket :', length_heartminutes)
        heartminutes_list = []

        for i in range(length_heartminutes):
            if len(heartminutes['bucket'][i]['dataset'][0]['point']) != 0:
                heartminutes_list.append(heartminutes['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal'])
            else:
                heartminutes_list.append(0)

        hrminute_cal_dict = {}

        current_date = start_date
        for day in range(length_heartminutes):
            formatted_date = current_date.strftime("%Y-%m-%d")
            hrminute_value = heartminutes_list[day]
            hrminute_cal_dict[formatted_date] = hrminute_value
            current_date += timedelta(days=1)
        print('hrminute_cal_dict :', hrminute_cal_dict)
        # data_obj = watch_data.objects.get(patient_id = patient_id)
        for date, hrminute in hrminute_cal_dict.items():
            # hrminute_obj = watch_data(patient_id = patient_id, date=date, heart_minutes = hrminute )
            # hrminute_obj.save()
            try:
                hrminute_obj = watch_data.objects.get(date = date, patient_id=patient_id)
                hrminute_obj.heart_minutes = hrminute
                hrminute_obj.save()
            except:
                hrminute_obj = watch_data(date = date, patient_id = patient_id, heart_minutes=hrminute)
                hrminute_obj.save()

    else:
        print(f"Request for heartminutes failed with status code: {response.status_code}")
        print(response.text)  

    # =============== Api request for Nutrition ==============
    params_nutrition = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.heart_minutes.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.nutrition",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_nutrition)
    if response.status_code == 200:
        nutrition = response.json() 
        # print('nutrition :', nutrition)
        length_nutrition = len(nutrition['bucket'])
        print('length of nutrition bucket :', length_nutrition)
        nutrition_list = []
        # for i in range(length_speed):
        #      nutrition_list.append(nutrition['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal']) 
        print('nutrition_list :', nutrition_list)
    else:
        print(f"Request for nutrition failed with status code: {response.status_code}")
        print(response.text)  

    # =============== Api request for location ==============
    # parameters for location
    params_location = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.activity.segment:com.google.android.gms:merge_activity_segments',
                            "dataTypeName": "com.google.location.sample",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            # 'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_location)
    if response.status_code == 200:
        location = response.json()  
        # print('location :', location)
        length_location = len(location['bucket'])
        print('length of location bucket :', length_location)
        # activity_list = []
        # for i in range(length_speed):
        #      activity_list.append(activity['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('activity_list :', activity_list)
    else:
        print(f"Request for location failed with status code: {response.status_code}")
        print(response.text)  

    print('patient_id of success :', patient_id)
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/successconnect.html', {'user_data':user_data})

def diabetesprediction(request):
    # if request.method == "POST":
    #     user_id = request.POST['userid']

        diabetes_modal_path = os.path.join(settings.BASE_DIR, 'User', 'prediction_model', 'diabetes_model.sav')
        print(diabetes_modal_path)
        diabetes_model = pickle.load(open(diabetes_modal_path, 'rb'))
        print('success')

        data = Patient_data.objects.get(patient_id = patient_id)

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
            return render(request, 'user/diabetesresult.html', context=context)
        else:
            result = 'Alert!! You are diabetic. Recommended: DR Test'
            color = 'red'
            context = {
                'result' : result,
                'color' : color 
            }
            result = 'Alert!! You are diabetic. Recommended: DR Test'
            print(5)
            return render(request, 'user/diabetesresult.html', context=context)

    # return render(request, 'user/diabetesprediction.html')

def hearthealthprediction(request):
        
        heart_modal_path = os.path.join(settings.BASE_DIR, 'User', 'prediction_model', 'heart_disease_model.sav')
        print(heart_modal_path)
        heart_model = pickle.load(open(heart_modal_path, 'rb'))
        print('success')

        data = Patient_data.objects.get(patient_id = patient_id)

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
            return render(request, 'user/hearthealthpredictorresult.html', context=context)
        else:
            result = 'Alert!! Your heart is at risk'
            color = 'red'
            context = {
                'result' : result,
                'color' : color 
            }
            print(5)
        return render(request, 'user/hearthealthpredictorresult.html', context=context)


def userprofile(request):
    if request.method  == "POST":
        fullname = request.POST['fullname']
        about = request.POST['about']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        print("image")
        image = request.FILES.get('profileimage')
        print("image got")
        print(settings.BASE_DIR)

        userinfo = Patient_data.objects.get(patient_id=patient_id)
        userinfo.fullname = fullname
        userinfo.image = image
        userinfo.about = about
        userinfo.age = age
        userinfo.gender = gender
        userinfo.fulladdress = address
        userinfo.phone = phone
        userinfo.email = email
        userinfo.save()
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/userprofile.html',  {'user_data' : user_data, 'data1_date' : data1_date, 'data1_steps' : data1_steps, 'data2_date' : data2_date, 'data2_steps' : data2_steps, 'data3_date' : data3_date, 'data3_steps' : data3_steps})

def edituserprofile(request):
    return render(request, 'user/edituserprofile.html')

def edithealthconditions(request):
    if request.method == "POST":
        datetime1 = request.POST['datetime1']
        diabetes = request.POST.get('diabetes')
        obesity = request.POST.get('obesity')
        cancer = request.POST.get('cancer')
        heartdisease = request.POST.get('heartdisease')
        stroke = request.POST.get('stroke')
        mentalhealth = request.POST.get('mentalhealth')
        asthama = request.POST.get('asthama')
        hearingloss = request.POST.get('hearingloss')
        arthritis = request.POST.get('arthritis')
        posttraumatic = request.POST.get('posttraumatic')
        hiv = request.POST.get('hiv')
        gastro = request.POST.get('gastro')

        hc_pd = Patient_data.objects.get(patient_id=patient_id)
        print('health_condition_data_patientid :', patient_id)
        print(datetime1, diabetes, obesity, cancer, heartdisease, stroke, mentalhealth, asthama, hearingloss, arthritis, posttraumatic, hiv, gastro)

        hc_obj = health_condition_data(patient_id = hc_pd, datetime=datetime1, diabetes=diabetes, cancer=cancer, obesity=obesity, heart_disease=heartdisease, stroke=stroke, mental_health=mentalhealth, asthama=asthama, hearing_loss=hearingloss, arthritis=arthritis, post_traumatic_stress_disorder=posttraumatic, hiv_aids=hiv, gastrointestinal_disorder=gastro)
        hc_obj.save()

        return render(request, 'user/edithealthsuccess.html')


    return render(request, 'user/edithealthconditions.html')

def editfeeltoday(request):
    if request.method == "POST":
        datetime1 = request.POST['datetime1']
        aciditydur = request.POST['aciditydur']
        acidityocc = request.POST['acidityocc']
        allergiesdur = request.POST['allergiesdur']
        allergiesocc = request.POST['allergiesocc']
        backpaindur = request.POST['backpaindur']
        backpainocc = request.POST['backpainocc']
        bodyachedur = request.POST['bodyachedur']
        bodyacheocc = request.POST['bodyacheocc']
        colddur = request.POST['colddur']
        coldocc = request.POST['coldocc']
        dentaldur = request.POST['dentaldur']
        dentalocc = request.POST['dentalocc']
        headachedur = request.POST['headachedur']
        headacheocc = request.POST['headacheocc']
        stomachdur = request.POST['stomachdur']
        stomachocc = request.POST['stomachocc']
        vomitingdur = request.POST['vomitingdur']
        vomitingocc = request.POST['vomitingocc']

        print('feel today data :', aciditydur, acidityocc, allergiesdur, allergiesocc)
        feel_pd = Patient_data.objects.get(patient_id=patient_id)

        feel_obj = todays_feel_data(patient_id=feel_pd, datetime=datetime1, acidity_duration=aciditydur, acidity_occurance=acidityocc, allergy_duration=allergiesdur, allergy_occurance=allergiesocc, backpain_duration=backpaindur, backpain_occurance=backpainocc, bodyache_duration=bodyachedur, bodyache_occurance=bodyacheocc, common_cold_duration=colddur, common_cold_occurance=coldocc, dental_pain_duration=dentaldur, dental_pain_occurance=dentalocc, headache_duration=headachedur, headache_occurance=headacheocc, stomachache_duration=stomachdur, stomachache_occurance=stomachocc, vomiting_duration=vomitingdur, vomiting_occurance=vomitingocc)
        feel_obj.save()
        return render(request, 'user/edithealthsuccess.html')

    return render(request, 'user/editfeeltoday.html')

def editregularmedications(request):
    if request.method == "POST":
        
        # user_id = request.POST['userid']
        medication1 = request.POST['medication1']
        medication2 = request.POST['medication2']
        medication3 = request.POST['medication3']
        medication4 = request.POST['medication4']
        medication5 = request.POST['medication5']
        syrup1name = request.POST['syrup1name']
        syrup1quantity = request.POST['syrup1quantity']
        syrup2name = request.POST['syrup2name']
        syrup2quantity = request.POST['syrup2quantity']
        syrup3name = request.POST['syrup3name']
        syrup3quantity = request.POST['syrup3quantity']
        datetime1 = request.POST['datetime1']

        print('patient_id :', patient_id)
        pd_obj = Patient_data.objects.get(patient_id = patient_id)
        med_obj = medication_data(patient_id = pd_obj, medication1 = medication1, medication2=medication2, medication3=medication3, medication4=medication4, medication5=medication5, syrup1name=syrup1name, syrup1quantity=syrup1quantity, syrup2name=syrup2name, syrup2quantity=syrup2quantity, syrup3name=syrup3name, syrup3quantity=syrup3quantity, datetime=datetime1)

        # med_obj = medication_data.objects.get(patient_id = patient_id)
        # med_obj.medication1 = medication1
        # med_obj.medication2 = medication2
        # med_obj.medication3 = medication3
        # med_obj.medication4 = medication4
        # med_obj.medication5 = medication5
        # med_obj.syrup1name = syrup1name
        # med_obj.syrup1quantity = syrup1quantity
        # med_obj.syrup2name = syrup2name
        # med_obj.syrup2quantity = syrup2quantity
        # med_obj.syrup3name = syrup3name
        # med_obj.syrup3quantity = syrup3quantity

        med_obj.save()
        return render(request, 'user/edithealthsuccess.html')
    return render(request, 'user/editregularmedications.html')

def editexercisedata(request):
    if request.method == "POST":
        datetime1 = request.POST["datetime1"]
        walk = request.POST["walk"]
        cycling = request.POST["cycling"]
        pranayam = request.POST["pranayam"]
        stairs = request.POST["stairs"]

        exe_pd = Patient_data.objects.get(patient_id=patient_id)

        exe_obj = exercise_data(patient_id=exe_pd, datetime=datetime1, walk=walk, cycling=cycling, pranayam=pranayam, stairs=stairs)
        exe_obj.save()

        return redirect('EditHealthSuccess')

    return render(request, 'user/editexcercisedata.html')

def iglu(request):
    return render(request, 'user/iglu.html')

def iframe2d(request):
    p_data = Patient_data.objects.get(patient_id=patient_id)
    Patient = f'{p_data.esio_patient_name}/{p_data.esio_folder_name}'
    return render(request, 'user/iframe2d.html', {'Patient':Patient})

def userhome(request):
    user_data = Patient_data.objects.get(patient_id=patient_id)

    try:
        last_pd = Patient_data.objects.get(patient_id=patient_id)
        last_entry = vitals_data.objects.filter(patient_id=last_pd).latest('datetime')
        pulserate = last_entry.pulserate
        respiratory = last_entry.respiratoryrate
        bp = last_entry.bp
        weight = last_entry.weight
        fbs = last_entry.bloodsugarfbs
        rbs = last_entry.bloodsugarrbs
    except:
        pulserate = 0
        respiratory = 0
        bp = 0
        weight = 0
        fbs = 0
        rbs = 0

    return render(request, 'user/index_na.html',  {'patient_id' : patient_id, 'user_data' : user_data, 'data1_date' : data1_date, 'data1_steps' : data1_steps, 'data2_date' : data2_date, 'data2_steps' : data2_steps, 'data3_date' : data3_date, 'data3_steps' : data3_steps, 
        'heart_point_1_5' : heart_point_1_5, 'heart_point_6_10' : heart_point_6_10, 'heart_point_11_15' : heart_point_11_15, 'heart_point_16_20' : heart_point_16_20, 'heart_point_21_25': heart_point_21_25, 'heart_point_26_30' : heart_point_26_30, 
        'avg_calburnt_1_5' : avg_calburnt_1_5, 'avg_calburnt_6_10' : avg_calburnt_6_10, 'avg_calburnt_11_15' :avg_calburnt_11_15, 'avg_calburnt_16_20' : avg_calburnt_16_20, 'avg_calburnt_21_25' : avg_calburnt_21_25, 'avg_calburnt_26_30' : avg_calburnt_26_30, 
        'avg_steps' : avg_steps, 'avg_hp' : avg_hp, 'avg_calburnt':avg_calburnt, 'pulserate':pulserate, 'respiratory':respiratory, 'bp':bp, 'weight':weight, 'fbs':fbs, 'rbs':rbs   })
    # return render(request, 'user/userhome.html')

def igluaccessdata(request):
    return render(request, 'user/igluaccessdata.html')

@csrf_exempt
def iglu_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')

            # Check the 'message' value and respond accordingly
            if message == 'glucose_lower':
                response_data = {'value': 90}
            elif message == 'glucose_normal':
                response_data = {'value': 100}
            elif message == 'glucose_higher':
                response_data = {'value': 120}
            elif message == 'spo2_lower':
                response_data = {'value': 90}
            elif message == 'spo2_normal':
                response_data = {'value': 95}
            elif message == 'spo2_higher':
                response_data = {'value': 100}
            else:
                response_data = {'error': 'Invalid query'}

            datetime1 = datetime.now()

            patient_obj = Patient_data.objects.get(patient_id=patient_id)
            iglu_obj = iglu_data(patient_id=patient_obj, glucoserbs = response_data, datetime=datetime1)
            iglu_data.save()

            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def userlogout(request):
    logout(request)
    return redirect('CharakHome')