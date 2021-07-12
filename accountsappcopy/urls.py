from django.contrib import admin
from django.urls import path, include

from accountsappcopy.views import hello_world, AccountCreateView

app_name ='accountsapp'
urlpatterns = [
    path('hello_world/',hello_world,name = 'hello_world'),
    #이떄 url path 를 만들어도 accountsappcopy app에는 url이 없다
    path('create/',AccountCreateView.as_view(),name='create')
]
