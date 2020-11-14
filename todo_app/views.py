from django.shortcuts import render


def homeVu(request):
    context = {
        'title' : 'Home',
    }
    return render(request,'index.html',context)

def signupVu(request):
    context = {
        'title' : 'Sign Up',
    }
    return render(request,'signup.html',context)

def loginVu(request):
    context = {
        'title' : 'Login',
    }
    return render(request,'login.html',context)