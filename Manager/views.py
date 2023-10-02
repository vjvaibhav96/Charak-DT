from django.shortcuts import render, redirect
from .models import Registered_Admin, Patient_data
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime

# dependencies for mirror
# import os
# import pickle
# import cv2
# import face_recognition
# import imutils
# from imutils.video import FPS

# uncomment below for smart mirror
# def create():
#     if os.path.exists("encodings1.pickle"):
#         print("loading encodings...")
#         data = pickle.loads(open("encodings1.pickle", "rb").read())
#     else:
#         data = {"encodings": [], "names": []}
#     print("Checking for new classes...")
#     people = os.listdir('dataset')
#     for i in people:
#         if i not in data['names']:
#             for j in os.listdir("dataset/"+i):
#                 print("processing image {}/{}".format(i, j))
#                 name = i
#                 image = cv2.imread('dataset/'+i+'/'+j)
#                 rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#                 boxes = face_recognition.face_locations(rgb, model="HOG")
#                 encodings = face_recognition.face_encodings(rgb, boxes, num_jitters=10)
#                 for encoding in encodings:
#                     data['encodings'].append(encoding)
#                     data['names'].append(name)
#     print("serializing encodings...")
#     f = open("encodings1.pickle", "wb")
#     f.write(pickle.dumps(data))
#     f.close()
#     return data

# Create your views here.
def index(request):
    return render(request, 'manager/index.html')

def signup(request):
    if request.method == "POST":
        print(request)
        # admin_id = request.POST.get('admin_id')
        managerfirstname = request.POST.get('managerfirstname')
        managermiddlename = request.POST.get('managermiddlename')
        managerlastname = request.POST.get('managerlastname')
        manageremail = request.POST.get('manageremail')
        managermobile = request.POST.get('managermobile')
        managerpassword = request.POST.get('managerpassword')
        managercpassword = request.POST.get('managercpassword')
        managerdob = request.POST.get('managerdob')
        managerqualification = request.POST.get('managerqualification')
        managerfacilityname = request.POST.get('managerfacilityname')
        managerstate = request.POST.get('managerstate')
        managerdistrict = request.POST.get('managerdistrict')
        managercity = request.POST.get('managercity')
        managerpin = request.POST.get('managerpin')
        managerdatetime = datetime.now()
        manager_flag = 0

        admin = Registered_Admin(mfirstname=managerfirstname, mmiddlename=managermiddlename, mlastname=managerlastname, memail=manageremail, mpassword=managerpassword, mcpassword=managercpassword, mmobile=managermobile, mdob=managerdob, mqualification=managerqualification, mstate=managerstate, mdistrict=managerdistrict, mcity=managercity, mpincode=managerpin, mfacilityname=managerfacilityname, mdatetime=managerdatetime, manager_flag=manager_flag)
        admin.save()

        auser = User.objects.create_user(username=manageremail, password=managerpassword, email=manageremail, first_name=managerfirstname)
        auser.save()

        # #create Admin 
        # registered_admin.save()
        # messages.success(request, "Your account has been created") 

        # if len(username) > 10:
        #     messages.error(request, "username must be under 10 characters only")
        #     return redirect('ManagerSignup')
        # if confirmpassword != password:
        #     messages.error(request, "Passwords do not match")
        #     return redirect('ManagerSignup')
        # if not username.isalnum():
        #     messages.error(request, "Username should only contain number and alphabates")
        #     return redirect('ManagerHome')

        # return render(request, "{% url 'CharakHome' %}" )
        return redirect("ManagerSingupSuccess")
    else:
        return render(request, 'manager/signup.html')

def managerlogin(request):
    if request.method == "POST":
        entered_username = request.POST.get('managerloginemail')
        entered_password = request.POST.get('managerloginpassword')
        # print(entered_username, entered_password)
        # return redirect('ManagerHome')

        # # authenticate the user
        user = authenticate(username=entered_username, password=entered_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('ManagerHome')
        else:
            messages.error(request, "Invalied Credentilas")
            # return redirect("#")
            return redirect("ManagerLogin")
    else:
        return render(request, 'manager/login.html')

# previous manager login method from login1.html page
# def managerlogin(request):
#     if request.method == "POST":
#         entered_username = request.POST.get('username')
#         entered_password = request.POST.get('password')

#         #authenticate the user
#         user = authenticate(username=entered_username, password=entered_password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully logged in")
#             return redirect('ManagerHome')
#         else:
#             messages.error(request, "Invalied Credentilas")
#             return redirect("ManagerLogin")
#     else:
#         return render(request, 'manager/login.html')

def attributes(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        age = request.POST.get('age')
        fulladdress = request.POST.get('fulladdress')
        gender = request.POST.get('gender')
        chestpaintype =  request.POST.get('chestpaintype')
        glucosevalue = request.POST.get('glucosevalue')
        bloodpressure = request.POST.get('bloodpressure')
        insulinvalue = request.POST.get('insulinvalue')
        bmi = request.POST.get('bmi')
        prediabetic = request.POST.get('prediabetic')
        dpf = request.POST.get('dpf')
        cholestrol = request.POST.get('cholestrol')
        dailyexercise = request.POST.get('dailyexercise')
        sleepinghabit  = request.POST.get('sleepinghabit')
        brushinghabit = request.POST.get('brushinghabits')

        #export data to Patient/User_data table
        
        user_attributes = Patient_data(fullname=fullname, email=email, age=age, fulladdress=fulladdress, gender=gender, chestpaintype=chestpaintype, glucosevalue=glucosevalue, bloodpressure=bloodpressure, insulinvalue=insulinvalue, bmi=bmi, prediabetic=prediabetic, dpf=dpf, cholestrol=cholestrol, dailyexercise=dailyexercise, sleepinghabits=sleepinghabit, brushinghabits=brushinghabit)
        user_attributes.save()
        return redirect('ManagerHome')
    return render(request, 'manager/attributes.html')

def prediction(request):
    return render(request, 'manager/prediction.html')

def manager_home(request):
    # from cryptography.fernet import Fernet ## library used for encryption and decryption
    # secret_key = Fernet.generate_key()
    # cipher_suite = Fernet(secret_key)

    if request.method == "POST":
        patientname = request.POST.get('uusername')
        patientemail = request.POST.get('uemail')
        # patientabhaid = request.POST.get('abhaid')
        patientpassword = request.POST.get('upassword')
        patientmobile = request.POST.get('umobile')
        patientimage = request.FILES.get('patientimage')
        enc_password = (patientpassword).encode('utf-8')
        enc_email = (patientemail).encode('utf-8')
        # hashed_password = cipher_suite.encrypt(enc_password)
        # hashed_email = cipher_suite.encrypt(enc_email)

        patient = User.objects.create_user(username=patientemail, email=patientemail, password=patientpassword, first_name=patientname)
        patient.save()
        data = Patient_data(fullname = patientname, email = patientemail, phone=patientmobile, password=patientpassword, image=patientimage, age=0, fulladdress='00', gender='00', chestpaintype=0, glucosevalue=0, bloodpressure=0, insulinvalue=0, bmi=0, prediabetic=0, dpf=0, cholestrol=0, dailyexercise=0, sleepinghabits=0, brushinghabits=0 )
        # data = Patient_data(fullname = patientname, email = patientemail, phone=patientmobile, abha_id = patientabhaid, password=patientpassword, image=patientimage, age=0, fulladdress='00', gender='00', chestpaintype=0, glucosevalue=0, bloodpressure=0, insulinvalue=0, bmi=0, prediabetic=0, dpf=0, cholestrol=0, dailyexercise=0, sleepinghabits=0, brushinghabits=0 )
        data.save()

        id = data.patient_id
        return render(request, 'manager/registorsuccess.html', {'ID' : id})
        # return render(request, 'manager/manager_home.html')
    # return render(request, 'manager/login.html', {'error_message': error_message})
    return render(request, 'manager/manager_home.html')

def managerlogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('CharakHome')

def managersingupsuccess(request):
    loginmodal = 1
    
    return render(request, 'manager/singupsuccess.html' )

# uncomment below for smart mirror
# def smartmirror(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         loc = 'dataset/'+ username
#         print(loc)
#         try:
#             os.makedirs(loc)
#             pass
#         except FileExistsError:
#             print("Directory with same name already exists!")
#         pic_no = 0
#         cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
#         while True:
#             ret, frame = cap.read()
#             frame = cv2.flip(frame, 1)
#             cv2.imshow('Video', frame)
#             if cv2.waitKey(10) & 0xFF == ord('c'):
#                 pic_no += 1
#                 cv2.imwrite(loc+'/'+str(pic_no)+'.jpg', frame)
#                 if(pic_no > 9):
#                     cap.release()
#                     cv2.destroyAllWindows()
#                     create()
#                     return
#     return render(request, 'manager/smartmirror.html')