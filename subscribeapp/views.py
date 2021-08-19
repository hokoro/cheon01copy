from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


class SubscriptionView(RedirectView):
    def get(self, request, *args, **kwargs): #게시판 정보와 user 정보
        user = request.user
        project= Project.objects.get(pk=kwargs['project_pk'])

        subscription = Subscription.objects.filter(user=user,project=project)

        #구독자 객체가 존재 하면
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user,project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail',kwargs={'pk':kwargs['project_pk']})

