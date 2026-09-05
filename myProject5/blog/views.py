from django.shortcuts import render
from datetime import  datetime

class User: 
    def __init__(self,name,age):
        self.name =  name
        self.age = age

def home (request):
    context = {
        "name" : "Ananjan Das Poddar",
        "age" : 19,
        "skills" : ["Python, Django, FastApi"],
        "user" : User("Ananjan",21),
        "blog" : {
            "title" : "Django template",
            "content" : "<b> This is Bold</b>",
            "created_at" : datetime(2026,9,3,16,40)
        },
        "empty_value" : None
    } 
    return render(request,"blog/home.html", context)