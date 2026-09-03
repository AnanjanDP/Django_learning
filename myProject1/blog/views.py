from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog home page")

def about(request):
    return HttpResponse("Blog About Page")

# Create your views here.
