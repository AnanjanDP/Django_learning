from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='shop-home'),
    path('about/',views.products,name='shop-product')
]