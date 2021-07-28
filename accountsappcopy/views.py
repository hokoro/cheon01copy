from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountsappcopy.decorators import account_ownership_required
from accountsappcopy.forms import AccountCreationForm
from accountsappcopy.models import HelloWorld


@login_required(login_url=reverse_lazy('accountsapp:login'))
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
        return render(request, 'accountsapp/hello_world.html', context={'data_list': data_list})
        # HttpResponse('Hello World')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    #success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'accountsapp/create.html'
    def get_success_url(self):
        return reverse('accountsapp:detail',kwargs= {'pk':self.object.pk})

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountsapp/detail.html'


has_ownership = [login_required,account_ownership_required]
@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    #success_url = reverse_lazy('accountsapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountsapp/update.html'
    def get_success_url(self):
        return reverse('accountsapp:detail',kwargs= {'pk':self.object.pk}) #accounts 는 계정이 바로 user 이기때문에 거치지 않고 바로 pk 를 받는다

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountsapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountsapp/delete.html'
