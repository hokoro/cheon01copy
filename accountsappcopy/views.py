from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountsappcopy.forms import AccountCreationForm
from accountsappcopy.models import HelloWorld


def hello_world(request):
    if request.user.is_authenticated: #계정의 로그인이 되있는 지 확인
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
    else:
        return HttpResponseRedirect(reverse('accountsapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name ='accountsapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountsapp/detail.html'
class AccountUpdateView(UpdateView):
    model = User
    form_class =  AccountCreationForm
    success_url = reverse_lazy('accountsapp:hello_world')
    context_object_name =  'target_user'
    template_name = 'accountsapp/update.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object() == request.user: #로기인 되있는지 확인 + 브라우저 에서 보낸 key = db 가 가지고 있는 키값이 같은지 호가인
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request,*args,**kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountsapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountsapp/delete.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request,*args,**kwargs)
        else:
            return HttpResponseForbidden()
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request,*args,**kwargs)
        else:
            return HttpResponseForbidden()
