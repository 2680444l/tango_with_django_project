from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# created a view called index
def index(request):
    return HttpResponse("Rango says hey there partner!")
