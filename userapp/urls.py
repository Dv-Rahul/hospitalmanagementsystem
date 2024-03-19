from django.urls import path
from . import views



urlpatterns = [
    path("",views.home),
    path('signup',views.patientsignup , name='patient-signup'),
    path("emergency/", views.emergency, name="emergencyurl"),
    path("contactus/", views.contactus, name="contactusurl"),
    path("login/", views.loginpage, name="loginurl"),
    path("home/", views.homepage, name="home"),
]