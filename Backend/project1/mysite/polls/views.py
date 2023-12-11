from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html',{})
   
def call(request):
    return render(request,"port.html")