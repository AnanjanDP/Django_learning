from django.shortcuts import render
from .models import YouTubeUser
from django.core.cache import cache

def users_list(request):
    users = cache.get('users_data') # getting data from cache
    if not users:
        print("Cache miss: Fetching data from other databases")
        users = YouTubeUser.objects.all()
        cache.set('users_data', users, timeout=300)
    else:
        print("cache hit: Fetching data from cache")

    return render(request, 'users_list.html',{'users':users})
