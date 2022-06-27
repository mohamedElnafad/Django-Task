from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, "website/home.html")


