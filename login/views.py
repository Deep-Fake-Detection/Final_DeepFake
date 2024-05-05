

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
@requires_csrf_token
# Create your views here.
def home(request):
    return render(request,'login.html')

def login(request):
    print(request)
    if(request=='GET'):
        email=request.GET['txt']
        password=request.GET['pas']
        print(email,password)
    if(request=='POST'):
        email=request.POST('txt')
        password=request.POST('pas')
        print(email,password)
        if(email=='vishnuv' and password=='1234'):
            return render(request,'model.html')
        else:
            return render(request,'login.html',{'valid':'Please enter a valid credentials !!'})
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
def logout(request):
    return render(request,'logout.html')