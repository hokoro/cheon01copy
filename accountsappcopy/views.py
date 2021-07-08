from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    if request.method == 'POST':
        return render(request,'accountsapp/hello_world.html',context={'text':'POST'})
    else:
        return render(request,'accountsapp/hello_world.html',context = {'text':'GET'})
    #HttpResponse('Hello World')