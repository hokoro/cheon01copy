from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountsappcopy.decorators import account_ownership_required
from accountsappcopy.forms import AccountCreationForm
from accountsappcopy.models import HelloWorld
from articleapp.models import Article





class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'accountsapp/create.html'

    def get_success_url(self):
        return reverse('accountsapp:detail', kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountsapp/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)


has_ownership = [login_required, account_ownership_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    # success_url = reverse_lazy('accountsapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountsapp/update.html'

    def get_success_url(self):
        return reverse('accountsapp:detail',
                       kwargs={'pk': self.object.pk})  # accounts 는 계정이 바로 user 이기때문에 거치지 않고 바로 pk 를 받는다


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('articleapp:list')
    context_object_name = 'target_user'
    template_name = 'accountsapp/delete.html'
