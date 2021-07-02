from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request,'accountsapp/hello_world.html')
    #HttpResponse('Hello World')