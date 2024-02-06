from django.shortcuts import render
from django.http import HttpResponse

# create your views here

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Paola Vallejo'})


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
