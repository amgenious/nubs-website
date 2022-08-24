from django.shortcuts import render
from .models import Audio
from .models import President

# Create your views here.
# def index (request):
#     audio = Audio.objects.all
#     return render(request, "sunday_sermon.html",{"audio":audio})
def index(request):
    return render(request, 'index.html')

def about(request):
    president = President.objects.all()
    return render(request,'about.html', {"president":president})

def wings(request):
    return render(request,'wings.html')

def gallery(request):
    return render(request,'gallery.html')

def academic(request):
    return render(request,'academic.html')

def sermon(request):
    return render(request,'sermon.html')

def sunday_sermon(request):
    audio = Audio.objects.all()
    return render(request,'sunday_sermon.html', {"audio":audio}) 

def tuesday_studies(request):
    audio = Audio.objects.all()
    return render(request,'tuesday_studies.html', {"audio":audio}) 

def thursday_prayers(request):
    audio = Audio.objects.all()
    return render(request,'thursday_prayers.html', {"audio":audio}) 

