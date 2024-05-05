from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# detector/views.py

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model

# # Load the pre-trained model
# model = load_model('forgery_detection_model.h5')

# def detect_forgery(image):
#     # Preprocess the image
#     image = cv2.resize(image, (224, 224))  # Assuming your model expects input size (224, 224)
#     image = image / 255.0  # Normalize

#     # Predict using the model
#     prediction = model.predict(np.array([image]))
#     return prediction[0][0]  # Assuming binary classification (real or fake)

# @csrf_exempt
# def process_image(request):
#     if request.method == 'POST' and 'image' in request.FILES:
#         # Get the image from the request
#         image = request.FILES['image'].read()
#         nparr = np.fromstring(image, np.uint8)
#         img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#         # Detect forgery
#         result = detect_forgery(img_np)

#         return JsonResponse({'result': result})
#     else:
#         return JsonResponse({'error': 'Invalid request'})


def model(request):
    return render(request,'model.html')