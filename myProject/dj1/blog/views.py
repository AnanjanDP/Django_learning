from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the blog homepage")

def about(request):
    a = 10+30
    return HttpResponse(f"About page: {a}")