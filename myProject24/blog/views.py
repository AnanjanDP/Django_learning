from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['username']='Mohit'
    request.session['course']='Django full course'
    return HttpResponse("Session data saved successfully")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course','Not enrolled')
    return HttpResponse(f"Username {username} , Enrolled course : {course}")

def delete_session(request):
    request.session.flush()
    return HttpResponse("All sessions are deleted successfully")