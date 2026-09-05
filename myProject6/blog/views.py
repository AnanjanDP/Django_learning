from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title" : "My second djnago template",
        "descriptions" : "Django is a high-level Python web framework",
        "author" : "yes",
        "created_at" : datetime(2026,9,4,23,3),
        "comments_count" : 5,
        "tags" : ["Django","Python","FastApi"],
        "price":100,
        "number":7,

    }
    return render(request,'blog/blog_details.html',{"post":post})
# Create your views here.
