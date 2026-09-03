from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Shop home page")

def products(request):
    return HttpResponse("Shop Products page")
# Create your views here.
