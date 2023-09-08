from django.shortcuts import render, redirect
from django.http import HttpResponse
from Manager.models import Patient_data


# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def userlogin(request):
    if request.method == "POST":
        # user_data = Patient_data.objects.get(all)
        user_email = request.POST['userloginemail']
        user_password = request.POST['userloginpassword']

        user_data = Patient_data.objects.get(email = user_email)
        global patient_id
        patient_id = user_data.patient_id
        # print(user_data.fullname)
        return render( request, 'user/index_na.html', {'user_data' : user_data} )
    return render(request, 'user/userlogin.html')

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
        return redirect('EditHealthSuccess')
    
    user_data = Patient_data.objects.get(patient_id=patient_id)
    return render(request, 'user/edithealthdata.html', {'user_data':user_data})

def edithealthsuccess(request):
    if request.method == "POST":
        return redirect( "{% url 'PatientHome' %}")
    return render(request, 'user/edithealthsuccess.html')

def connectsmartwatch(request):
    return render(request, 'user/connectsmartwatch.html')

def diagnostictool(request):
    return render(request, 'user/diagnostictool.html')
