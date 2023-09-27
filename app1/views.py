from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def IndexPage(request):
    return render(request,'index.html')

def SignupPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # print(form, 'FORM')
        if form.is_valid():
            print("OKOKOK")
            form.save()
            return render(request, 'auth-login-basic.html')
        
    else:
        form = UserCreationForm()
    return render(request, 'auth-register-basic.html', {'form': form})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user, username, password, "OOOO")
        if user is not None:
            login(request, user)
            # print(user,'GOIT')
            return redirect('index')  # Redirect to the 'home' URL name on successful login
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'auth-login-basic.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def ForgotPasswordPage(request):
    
    return render(request, 'auth-forgot-password-basic.html')
