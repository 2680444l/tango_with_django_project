from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# created a view called index
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

def index(request):
    # the 'boldmessage' is in the template in html file
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return a rendered resonse to send to the client. Will be smashed together and returned with a HttpResponse
    return render(request, 'rango/index.html', context=context_dict)
