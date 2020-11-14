from django.urls import path
from django.conf import settings
from todo_app import views

urlpatterns = [
    path('',views.homeVu,name='homepage'),
    path('register/',views.signupVu,name='register'),
    path('login/',views.loginVu,name='login')
]