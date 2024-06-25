from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import College
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def add(request,a,b):
    c=a+b
    return HttpResponse('The addition of 2 numbers is'+str(c))

def College_list(request):
    Colleges=College.objects.all()

    return render(request,'College_list.html',{'Colleges':Colleges})