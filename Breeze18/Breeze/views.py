from django.shortcuts import render
from .models import Event

# Create your views here.

def home(request):
    return render(request, 'index.html')

def specificEventView(request, category, subcategory):
    #return all events listed under a category and subcategory
    #see "sample.html" for usage
    events = Event.objects.filter(category=category[0]).filter(subCategory=subcategory)
    context  = {'events': events}
    return render(request, 'sample.html', context=context)

def sponsor(request):
    return render(request, 'help/sponsor.html')

#change following three
def technical(request):
    return render(request, 'events/technical.html')

def cultural(request):
    return render(request, 'events/cultural.html')

def sports(request):
    return render(request, 'events/sports.html')
#change above three


def accomodation(request):
    return render(request, 'help/accomodation.html')

def transport(request):
    return render(request, 'help/transport.html')

def hospitality(request):
    return render(request, 'help/hospitality.html')
