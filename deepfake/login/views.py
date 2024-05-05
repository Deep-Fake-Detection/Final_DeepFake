

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
@requires_csrf_token
# Create your views here.
def home(request):
    if(request=='GET'):
        email=request.GET['txt']
        password=request.GET['pass']
    if(request=='POST'):
        email=request.POST('txt')
        password=request.POST('pass')
        print(email,password)
        if(email=='vishnuv' and password=='1234'):
            return redirect('login')
    return render(request,'login.html')

def login(request):
    return render(request,'model.html')

def register(request):
    return redirect('register')
def logout(request):
    return render(request,'logout.html')