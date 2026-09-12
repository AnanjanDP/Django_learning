from django.shortcuts import render
from .models import UserProfille
from django.core.cache import cache

def user_profile_list(request):
    users_data = cache.get('users_data')
    if users_data is None:
        print("Fetching data from other databases")
        users_data = UserProfille.objects.all()
        cache.set('users_data', users_data) #timeout=300)

    else:
        print("Fetching data from cache")

    return render(request, 'user_profile_list.html', {'users':users_data})