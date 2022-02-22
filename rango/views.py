from multiprocessing import context
from django.shortcuts import render

# Import the Category model from models.py
from rango.models import Category
from rango.models import Page

# Create your views here.
from django.http import HttpResponse

# created a view called index
# this is for the main page view
def index(request):
    # retrieve the top 5 likes in descending order
    # pass a reference to the list
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # render the response and send it
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # no need to use context dictionary
    return render(request, 'rango/about.html')