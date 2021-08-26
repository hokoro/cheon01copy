from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationsForm
from profileapp.models import Profile


#login 여부
@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationsForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountsapp:detail',kwargs = {'pk':self.object.user.pk}) #연결된 계정의 주소 를 가져와야 돼서 클래스로는 pk 못받음

#profile update 는 인증 과정이 필요
@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationsForm
    context_object_name = 'target_profile'
    #success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountsapp:detail',kwargs={'pk':self.object.user.pk})