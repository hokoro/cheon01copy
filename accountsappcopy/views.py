from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountsappcopy.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input')  # input 으로 입력 한 데이터 를 post.get 을 사용해 얻어 온다

        new_data = HelloWorld()
        new_data.text = temp  # client 로 받아온 data 를 db 모델에 저장한다.
        new_data.save()  # client 로 받은 데이터를 실제 db 에 저장
        '''
        data_list = HelloWorld.objects.all()
        return render(request,'accountsapp/hello_world.html',context={'data_list':data_list})
        '''
        return HttpResponseRedirect(reverse('accountsapp:hello_world'))
    else:
        data_list = HelloWorld.objects.all()
        return render(request,'accountsapp/hello_world.html',context = {'data_list':data_list})
    #HttpResponse('Hello World')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name ='accountsapp/create.html'