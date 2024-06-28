
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth.models import User, auth
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import login1

# views.py
import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseServerError
from tensorflow.keras.models import load_model


import cv2
import numpy as np

def generate_new_csrf_token(request):
    # Generate a new CSRF token
    new_token = get_token(request)

    # Return the new CSRF token as JSON response
    return JsonResponse({'csrf_token': new_token})




# Create your views here.



def home(request):
    return render(request,'login.html')


def login(request):
    if request.method =='GET':
        email=request.GET['txt']
        password=request.GET['pas']
        print(request.GET)
        print(email,password)
        if email == '' and password=='':
            return render(request,'login.html',{'blank1':'Please enter your credentials !'})
        if email=='vishnuv' and password=='1234':
            return render(request,'model.html',{'user':email})
        else:
            return render(request,'login.html',{'blank':'Please enter valid credentials !','b':'Please register !'})
        
    return render(request,'login.html')

def detect_forgery(image):
       # Preprocess the image
   image = cv2.resize(image, (224, 224))  # Assuming your model expects input size (224, 224)
   image = image / 255.0  # Normalize
       # Predict using the model
   prediction = model.predict(np.array([image]))
   return prediction[0][0]

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    return img

def predict_deepfake(image_path):
    img = preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    if prediction[0][0] > 0.5:
        return "Deepfake"
    else:
        return "Non Deepfake"
    
@csrf_exempt 
def register(request):
    return render(request,'register.html')
def model(request):
    print(request)
    if(request.method=='GET'):
        try:
            model_path = os.path.join(settings.STATIC_ROOT, 'densenet201_model.h5')    
            if not os.path.exists(model_path):
                raise FileNotFoundError("Model file not found at specified path.")           
            model = load_model(model_path)
            input1 = model.predict(request.GET('file-upload-input'))
            deepfake=predict_deepfake(input1)
            return render(request, 'model.html', {'deepfake': deepfake})
        except FileNotFoundError:
            # Handle the case where the model file is not found
            return HttpResponseServerError("Model file not found. Please make sure the model file exists.")
        except OSError as e:
            # Handle other OS-related errors
            return HttpResponseServerError(f"An error occurred while loading the model: {e}")
        except Exception as e:
            # Handle any other unexpected errors
            return HttpResponseServerError(f"An unexpected error occurred: {e}")
    if(request.method=='POST'): 
         return render(request,'model.html')
        
    return render(request,'model.html')


def toregister(request):
    print('toregister : ',request)
    if request.method == 'POST':
        name=request.POST.get('text')
        password1=request.POST.get('pas1')
        password2=request.POST.get('pas2')
        print(password2,password1)
        if password1 == password2 and password1 != '':
            obj=login1(username=name,password=password1)
            obj.save()
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'name':'password not maching !'})
    else:
        return render(request,'register.html')
def logout(request):
    return render(request,'logout.html')