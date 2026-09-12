from django.contrib import admin
from .models import UserProfille
@admin.register(UserProfille)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','email','subscribers')
    