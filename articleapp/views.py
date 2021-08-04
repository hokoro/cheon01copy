from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article



class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'articleapp/create.html'

    def form_valid(self, form): #검증이 끝나면 마지막에 실행되는 메소드
        form.instance.writer = self.request.user #글이 작성 되면 요청을 보내는 유저의 정보를 보낸다
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})