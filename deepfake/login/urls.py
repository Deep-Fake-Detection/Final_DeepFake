

# app page 
from .views import generate_new_csrf_token
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('toregister',views.toregister,name="toregister"),
    path('model',views.model,name="model"),
    path('logout',views.logout,name="logout"),
]
 