from django.shortcuts import render

# Create your views here.

    #sponsor accmodation, hospitality, transportation


def home(request):
    return render(request, 'index.html')

def login(request):
    pass

def register(request):
    pass

def sponsor(request):
    return render(request, 'base.html')

def accomodation(request):
    return render(request, 'accomodation.html')

def transport(request):
    return render(request, 'base.html')

def hospitality(request):
    return render(request, 'base.html')
