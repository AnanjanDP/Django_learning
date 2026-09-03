from django.urls import path, re_path
from . import views

urlpatterns =[
    path('post/<int:post_id>/', views.post_details, name =  'post_details' ),    
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('article/<int:year>/<str:month>/<str:days>/', views.article_details, name ='article_details'),
    #use re-path from pattern matching
    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_years, name ='article_by_years')
]