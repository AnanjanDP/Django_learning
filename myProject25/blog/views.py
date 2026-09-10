from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse('Cookie set successfully')
    response.set_cookie('username', 'Mohit Kumar', max_age = 60*60*24*7)
    response.set_cookie('course', 'Django Full Course', max_age= 60*60*24)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username','Guest')
    course =  request.COOKIES.get('course','No Courses Selected')
    if 'username' in request.COOKIES:
        return HttpResponse(f"Username: {username} and Course {course}")
    else:
        return HttpResponse("No cookies found")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted Successfully")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response
