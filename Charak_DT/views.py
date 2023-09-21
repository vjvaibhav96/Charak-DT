from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

def index(request):
    return render(request, 'index_flexor.html')

def esiofy(request):
    return render(request, 'esiofy.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject1 = request.POST.get('subject')
        message1 = request.POST.get('message')

        subject = 'New querry received for Charak'
        message = f'     Name : Mr. {name} \n     Email : {email} \n     Subject : {subject1} \n     Querry : {message1} '
        from_email = email
        recipient_list = ['vaibhav.drishticps@iiti.ac.in']

        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'contactsuccess.html')
    
def contactsuccess(request):
    return render(request, 'contactsuccess.html')

def healthcareprovider(request):
    return render(request, 'healthcareprovider.html')