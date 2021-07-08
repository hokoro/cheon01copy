from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountsappcopy.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input')  # input 으로 입력 한 데이터 를 post.get 을 사용해 얻어 온다

        new_data = HelloWorld()
        new_data.text = temp  # client 로 받아온 data 를 db 모델에 저장한다.
        new_data.save()  # client 로 받은 데이터를 실제 db 에 저장
        return render(request,'accountsapp/hello_world.html',context={'new_data':new_data})
    else:
        return render(request,'accountsapp/hello_world.html',context = {'text':'GET METHOD'})
    #HttpResponse('Hello World')