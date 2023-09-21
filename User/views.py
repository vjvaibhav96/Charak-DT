from django.shortcuts import render, redirect
from django.http import HttpResponse
from Manager.models import Patient_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 


# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def userlogin(request):
    if request.method == "POST":
        # user_data = Patient_data.objects.get(all)
        user_email = request.POST['userloginemail']
        user_password = request.POST['userloginpassword']

        # authenticate the user
        user = authenticate(username=user_email, password=user_password)

        if user is not None:
            print('user authenticated')
            login(request, user)
            # messages.success(request, "Successfully logged in")

            data = Patient_data(email = user_email)

            user_data = Patient_data.objects.get(email = user_email)
            global patient_id
            patient_id = user_data.patient_id
            # print(user_data.fullname)
            return render( request, 'user/index_na.html', {'user_data' : user_data} )
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

def userhome(request):
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/index_na.html', {'user_data':user_data})
    # return render(request, 'user/userhome.html')

def accesshealthdata(request):
    if request.method == "POST":
        return redirect('HealthData')
    return render(request, 'user/accesshealthdata.html')

def healthdata(request):
    print(patient_id)
    id  = patient_id
    user_hdata = Patient_data.objects.get(patient_id=id)
    print(user_hdata)
    return render(request, 'user/healthdata.html', {'user_hdata' : user_hdata})

def edithealthdata(request):
    if request.method == "POST":
        print('12358')
        userid = request.POST['userid']
        chestpaintype = request.POST['chestpaintype']
        glucose = request.POST['glucose']
        heartrate = request.POST['heartrate']
        bloodpressure = request.POST['bloodpressure']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        prediabetic = request.POST['prediabetic']
        dpf = request.POST['dpf']
        cholestrol = request.POST['cholestrol']
        dailyexercisehr = request.POST['dailyexercisehr']
        sleepinghabit = request.POST['sleepinghabit']
        brushinghabit = request.POST['brushinghabit']

        print(userid, bmi, bloodpressure, glucose)
        updatedata = Patient_data.objects.get(patient_id = userid)
        updatedata.chestpaintype = chestpaintype
        updatedata.glucosevalue = glucose
        updatedata.bloodpressure = bloodpressure
        updatedata.insulinvalue = insulin
        updatedata.bmi = bmi
        updatedata.prediabetic = prediabetic
        updatedata.dpf = dpf
        updatedata.cholestrol = cholestrol
        updatedata.dailyexercise = dailyexercisehr
        updatedata.brushinghabits = brushinghabit
        updatedata.sleepinghabits = sleepinghabit
        updatedata.save()
        # print('updatedata :', updatedata)
        return redirect('EditHealthSuccess')
    
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/edithealthdata.html', {'user_data':user_data})

def edithealthsuccess(request):
    if request.method == "POST":
        '''userid, chestpaintype, glucose, heartrate, bloodpressure, insulin, bmi, prediabetic, dpf, cholestrol, dailyexercisehr, sleepinghabit, brushinghabit '''

        return redirect( "{% url 'PatientHome' %}")
    return render(request, 'user/edithealthsuccess.html')

def connectsmartphone(request):
    from oauthlib.oauth2 import WebApplicationClient
    from requests_oauthlib import OAuth2Session
    from datetime import datetime
    import os
    # Define the Google Fit API endpoints
    authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
    token_url = 'https://accounts.google.com/o/oauth2/token'

    if request.method == "POST":
        global googleclientid, googlesecretkey, userredirecturi
        googleclientid = request.POST['googleclientid']
        googlesecretkey = request.POST['googleclientsecretkey']
        userredirecturi = request.POST['userredirecturi']
        userid = request.POST['userid']
        print('googleclientid', googleclientid)
        print('googlesecretkey', googlesecretkey)
        print('userredirecturi', userredirecturi)

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

    return render(request, 'user/connectsmartphone.html')

def successconnect(request):
    from oauthlib.oauth2 import WebApplicationClient
    from requests_oauthlib import OAuth2Session
    from datetime import datetime
    import requests
    print('1234')
    token_url = 'https://accounts.google.com/o/oauth2/token'
    
    # Define your start and end dates
    start_date = datetime(2023, 9, 20)
    end_date = datetime(2023, 9, 21)

    # Convert the dates to Unix timestamps in milliseconds
    start_timestamp = int(start_date.timestamp()) * 1000
    end_timestamp = int(end_date.timestamp()) * 1000

    # Handle the authorization response
    # authorization_response = request.path
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
        steps = response.json()  # If the response contains JSON data
        length = len(steps['bucket'])
        stepcount = []
        # for i in range(length):
        #     stepcount.append(steps['bucket'][i]['dataset'][0]['point'][0]['value'][0]['intVal'])
        # print('stepcount :', stepcount)

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Heart Rate ==============

    # parameters for heartrate
    params_heartrate = {
        "aggregateBy": [{ 
                            "dataTypeName": "com.google.heart_rate.bpm",
                        }],
                            'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }
    
    # Make the API request for heartrate
    response = requests.post(api_url, headers=headers, json=params_heartrate)
    if response.status_code == 200:
        heartrate = response.json()  # If the response contains JSON data
        print('heartrate :', heartrate)
        length_hr = len(steps['bucket'])
        print('length of heartrate bucket :', length_hr)
        # uncomment this once the data is added to the google apis
        # heartrates_list = []
        # for i in range(length):
        #     heartrates_list.append(heartrate['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal'])
        # print('heartrates_list :', heartrates_list)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging   


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
        distance = response.json()  # If the response contains JSON data
        print('distance :', distance)
        length = len(distance['bucket'])
        print('length of distance bucket :', distance)
        # list
        # list_distance = []
        # for i in range(length):
        #     list_distance.append(distance['bucket'][i]['dataset'][0]['point'][0]['value'][0]['intVal'])
        # print('list_distance :', list_distance)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for calories expended ==============
    # parameters for calories expended
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
        calories = response.json()  # If the response contains JSON data
        length_calories = len(calories['bucket'])
        print('length of calories bucket :', length_calories)
        calories_list = []
        # for i in range(length_calories):
        #     calories_list.append(calories['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal'])
        # print('calories_list :', calories_list)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for speed ==============
    # parameters for speed
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
        speed = response.json()  # If the response contains JSON data
        length_speed = len(speed['bucket'])
        print('length of speed bucket :', length_speed)
        # speed_list = []
        # for i in range(length_speed):
        #      speed_list.append(speed['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('speed_list :', speed_list)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for activity segment ==============
    # parameters for activity
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
        activity = response.json()  # If the response contains JSON data
        print('activity :', activity)
        length_activity = len(speed['bucket'])
        print('length of activity bucket :', length_activity)
        # activity_list = []
        # for i in range(length_speed):
        #      activity_list.append(activity['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('activity_list :', activity_list)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for weight ==============
    # parameters for weight
    params_weight = {
        "aggregateBy": [{ 
                            # "dataSourceId": 'derived:com.google.weight.summary:com.google.android.gms:aggregated',
                            "dataTypeName": "com.google.weight",
                        }],
                            # 'bucketByTime': { 'durationMillis': 86400000 },
                            'startTimeMillis': str(start_timestamp),
                            'endTimeMillis': str(end_timestamp),
                        }

    response = requests.post(api_url, headers=headers, json=params_weight)
    if response.status_code == 200:
        weight = response.json()  # If the response contains JSON data
        print('weight :', weight)
        length_weight = len(weight['bucket'])
        print('length of weight bucket :', length_weight)
        # weight_list = []
        # for i in range(length_weight):
        #      weight_list.append(weight['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('activity_list :', weight_list)
    else:
        print(f"Request for weight failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Blood Pressure ==============
    # parameters for blood pressure
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
        bloodpressure = response.json()  # If the response contains JSON data
        print('bloodpressure :', bloodpressure)
        length_bloodpressure = len(bloodpressure['bucket'])
        print('length of bloodpressure bucket :', length_bloodpressure)
        # activity_list = []
        # for i in range(length_speed):
        #      activity_list.append(activity['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('activity_list :', activity_list)
    else:
        print(f"Request for bloodpressure failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Blood Glucose ==============
    # parameters for blood Glucose
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
        bloodglucose = response.json()  # If the response contains JSON data
        print('bloodglucose :', bloodglucose)
        length_bloodglucose = len(bloodglucose['bucket'])
        print('length of bloodglucose bucket :', length_bloodglucose)
        # bloodglucose_list = []
        # for i in range(length_speed):
        #      bloodglucose.append(glucose['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('bloodglucose_list :', bloodglucose_list)
    else:
        print(f"Request for bloodglucose failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Oxygen Saturation ==============
    # parameters for Oxygen Saturation
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
        oxygensaturation = response.json()  # If the response contains JSON data
        print('oxygensaturation :', oxygensaturation)
        length_oxygensaturation = len(oxygensaturation['bucket'])
        print('length of oxygensaturation bucket :', length_oxygensaturation)
        # oxygensaturation_list = []
        # for i in range(length_speed):
        #      oxygensaturation_list.append(oxygensaturation['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('oxygensaturation_list :', oxygensaturation_list)
    else:
        print(f"Request for oxygensaturation failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Body Temperature ==============
    # parameters for Body Temperature
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
        temperature = response.json()  # If the response contains JSON data
        print('temperature :', temperature)
        length_temperature = len(temperature['bucket'])
        print('length of temperature bucket :', length_temperature)
        # temperature_list = []
        # for i in range(length_speed):
        #      temperature_list.append(temperature['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('temperature_list :', temperature_list)
    else:
        print(f"Request for temperature failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Heart Minutes ==============
    # parameters for Heart Minutes
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
        heartminutes = response.json()  # If the response contains JSON data
        print('heartminutes :', heartminutes)
        length_heartminutes = len(heartminutes['bucket'])
        print('length of heartminutes bucket :', length_heartminutes)
        # heartminutes_list = []
        # for i in range(length_speed):
        #      heartminutes_list.append(heartminutes['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal']) 
        # print('heartminutes_list :', heartminutes_list)
    else:
        print(f"Request for heartminutes failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

    # =============== Api request for Nutrition ==============
    # parameters for Nutrition
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
        nutrition = response.json()  # If the response contains JSON data
        print('nutrition :', nutrition)
        length_nutrition = len(nutrition['bucket'])
        print('length of nutrition bucket :', length_nutrition)
        nutrition_list = []
        # for i in range(length_speed):
        #      nutrition_list.append(nutrition['bucket'][i]['dataset'][0]['point'][0]['value'][0]['fpVal']) 
        print('nutrition_list :', nutrition_list)
    else:
        print(f"Request for nutrition failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging



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
        location = response.json()  # If the response contains JSON data
        print('location :', location)
        length_location = len(location['bucket'])
        print('length of location bucket :', length_location)
        # activity_list = []
        # for i in range(length_speed):
        #      activity_list.append(activity['bucket'][i]['dataset'][0]['point'][0]['value'][j]['fpVal']) #for j = 'value' has 3 dict objects need to run the loop their as well
        # print('activity_list :', activity_list)
    else:
        print(f"Request for location failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging


    # Handle the response data as needed
    print('patient_id of success :', patient_id)
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/successconnect.html', {'user_data':user_data})

def diagnostictool(request):
    return render(request, 'user/diagnostictool.html')

def userlogout(request):
    logout(request)
    return redirect('CharakHome')

def userprofile(request):
    if request.method  == "POST":
        # image = request.POST['image']
        fullname = request.POST['fullname']
        about = request.POST['about']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']

        userinfo = Patient_data.objects.get(patient_id=patient_id)
        userinfo.fullname = fullname
        # userinfo.image = image
        userinfo.about = about
        userinfo.age = age
        userinfo.gender = gender
        userinfo.fulladdress = address
        userinfo.phone = phone
        userinfo.email = email
        userinfo.save()
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/userprofile.html', {'user_data':user_data})

def edituserprofile(request):
    return render(request, 'user/edituserprofile.html')