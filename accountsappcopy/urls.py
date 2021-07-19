from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountsappcopy.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, \
    AccountDeleteView

app_name ='accountsapp'
urlpatterns = [
    path('hello_world/',hello_world,name = 'hello_world'),
    path('login/',LoginView.as_view(template_name = 'accountsapp/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    #이떄 url path 를 만들어도 accountsappcopy app에는 url이 없다
    path('create/',AccountCreateView.as_view(),name='create'),
    path('detail/<int:pk>',AccountDetailView.as_view(),name = 'detail'),
    path('update/<int:pk>',AccountUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>',AccountDeleteView.as_view(),name = 'delete'),
]
