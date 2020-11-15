from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as loginUser,logout
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homeVu(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todos = Todo.objects.filter(user=user)
    context = {
        'title' : 'Home',
        'form': form,
        'todos': todos,
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
def add_todos(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("homepage")
        else: 
            return render(request ,'index.html' , context={'form' : form})

def signupVu(request):
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'title' : 'Sign Up',
        'form' : form,
    }
    return render(request,'signup.html',context)

def loginVu(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user  = authenticate(username=username,password=password)

            if user is not None:
                loginUser(request,user)
                return redirect('homepage')
            
            else:
                messages.info(request,'Username or password is incorrect')
        
    context = {'form':form}
    return render(request,'login.html',context)

def logoutVu(request):
    logout(request)
    return redirect('login')

def deleteVu(request,pk):
    todo = Todo.objects.get(id=pk).delete()
    return redirect('homepage')
    context = {
        'todo': todo,
    }
    return render(request,'index.html',context)

def statusVu(request,pk,status):
    todo = Todo.objects.get(id=pk)
    todo.status = status
    todo.save()
    return redirect("homepage")
    