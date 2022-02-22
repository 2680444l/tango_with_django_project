from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# created a view called index
def index(request):
    # Refer to the TwD book for more information on how this updated view works.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # no need to use context dictionary
    return render(request, 'rango/about.html')