from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1> welcome to doctor app <h1>")


from django.shortcuts import render

# Create your views here.
