from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationsForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationsForm
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountsapp:detail',kwargs = {'pk':self.object.user.pk}) #연결된 계정의 주소 를 가져와야 돼서 클래스로는 pk 못받음

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationsForm
    context_object_name = 'target_profile'
    #success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountsapp:detail',kwargs={'pk':self.object.user.pk})