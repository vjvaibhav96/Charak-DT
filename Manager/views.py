from django.shortcuts import render, redirect
from .models import Registered_Admin, Patient_data
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime

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
        print(entered_username, entered_password)
        return redirect('ManagerHome')

        # # authenticate the user
        # user = authenticate(username=entered_username, password=entered_password)

        # if user is not None:
        #     login(request, user)
        #     messages.success(request, "Successfully logged in")
        #     return redirect('ManagerHome')
        # else:
        #     messages.error(request, "Invalied Credentilas")
        #     return redirect("#")
            # return redirect("ManagerLogin")
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

        #export data to User_data table
        
        user_attributes = Patient_data(fullname=fullname, email=email, age=age, fulladdress=fulladdress, gender=gender, chestpaintype=chestpaintype, glucosevalue=glucosevalue, bloodpressure=bloodpressure, insulinvalue=insulinvalue, bmi=bmi, prediabetic=prediabetic, dpf=dpf, cholestrol=cholestrol, dailyexercise=dailyexercise, sleepinghabits=sleepinghabit, brushinghabits=brushinghabit)
        user_attributes.save()
        return redirect('ManagerHome')
    return render(request, 'manager/attributes.html')

def prediction(request):
    return render(request, 'manager/prediction.html')

def manager_home(request):
    # return render(request, 'manager/login.html', {'error_message': error_message})
    return render(request, 'manager/manager_home.html')

def managerlogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('CharakHome')

def managersingupsuccess(request):
    loginmodal = 1
    
    return render(request, 'manager/singupsuccess.html' )