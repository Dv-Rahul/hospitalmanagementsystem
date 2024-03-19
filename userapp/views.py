from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Signup, ContactModel


def home(request):
    #return HttpResponse("<h1> welcome to user app <h1>")
 return render(request,'userapp/h'
                       'ome.html')

from django.shortcuts import render

def patientsignup(request):
    if request.method == 'POST':
        username = request.POST['username'];
        email = request.POST['email'];
        password = request.POST['password'];
        confrimpassword = request.POST['confrimpassword'];
        patient = Signup(username=username,email=email,password=password,confrimpassword=confrimpassword)
        patient.save()
        return render(request,'userapp/signup.html', )
    return render(request,'userapp/signup.html')

def homepage(request):
    return render(request,'userapp/home.html' , )

def loginpage(request):
    return render(request,'userapp/login.html' , )


# def loginpage(request):
#     if request.user.is_authenticated:
#        x   return redirect("/")
#     else:
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 user1 = Applicant.objects.get(user=user)
#
#                 if user1.type == "applicant":
#                     login(request, user)
#                     return redirect("/user_homepage")
#             else:
#                 thank = True
#                 return render(request, "user_login.html", {"thank": thank})
#     return render(request, "login.html")

def emergency(request):
    return render(request,'userapp/Emergency.html' ,)


def contactus(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        comment = request.POST['comment']
        email = request.POST['email']
        subject = "If you have any query regarding TTMS"
        comment1 = comment + " This is System generated mail. So donot respond to this mail"

        data = ContactModel(firstname=firstname,lastname=lastname,comment=comment,email=email)
        data.save()
        send_mail(
            subject,
            comment1,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently= False
        )
        return HttpResponse("<h1 align=center>Mail Sent Successfully</h1>")
    return render(request,"userapp/contactus.html")