from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


class SubscriptionView(RedirectView):
    def get(self, request, *args, **kwargs):  # 게시판 정보와 user 정보
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])

        subscription = Subscription.objects.filter(user=user, project=project)

        # 구독자 객체가 존재 하면
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']})


class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self):
        project_list = Subscription.objects.filter(user = self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=project_list)

        return article_list