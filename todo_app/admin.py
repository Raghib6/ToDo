from django.contrib import admin
from .models import Todo


class AdminTodo(admin.ModelAdmin):
    list_display = ['user','title','priority','date','status']

admin.site.register(Todo,AdminTodo)