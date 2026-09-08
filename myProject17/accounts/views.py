from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

#register page
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) #auto-login 
            messages.success(request,'Registration successful. You can login in now')
            return redirect('dashboard')
        else:
            messages.error(request,'Registration failed. Please retry')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})  


#login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Login Failed. Invalid Username or Password')
    return render(request,'accounts/login.html')


#logout page 
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


#dashboard page
@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')