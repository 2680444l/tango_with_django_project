from multiprocessing import context
from tokenize import Name
from django.shortcuts import render

# Import the Category model from models.py
from rango.models import Category
from rango.models import Page

# Create your views here.
from django.http import HttpResponse

# a def function represents a view
# created a view called index
# this is for the main page view
def index(request):
    # retrieve the top 5 likes in descending order
    # pass a reference to the list
    category_list = Category.objects.order_by('-likes')[:5]
    # exercise: add page list for most views
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # excersie: add page list for most views
    context_dict['pages'] = page_list

    # render the response and send it
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # no need to use context dictionary
    return render(request, 'rango/about.html')

# pass category_name_slug as a value in
# must take at least one parameter, request
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # if categories are not found, then display "no category"
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)