from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index_flexor.html')

def esiofy(request):
    return render(request, 'esiofy.html')

