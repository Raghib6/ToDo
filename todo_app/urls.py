from django.urls import path
from django.conf import settings
from todo_app import views

urlpatterns = [
    path('',views.homeVu,name='homepage'),
    path('register/',views.signupVu,name='register'),
    path('login/',views.loginVu,name='login'),
    path('logout/',views.logoutVu,name='logout'),
    path('add_todo/',views.add_todos,name='add_todo'),
    path('delete_todo/<str:pk>/',views.deleteVu,name='delete_todo'),
    path('change_status/<str:pk>/<str:status>/',views.statusVu,name='change_status'),
]