from django.urls import path
from .views import *


urlpatterns = [
    path('',blog,name='blog'),
    path('post/search/',search,name='searchblog'),
    path('newsettler/',newsettler,name='newsettler'),
    path('post/<id>/',blog_post,name='blogpost'),
    path('post/category/<id>/',category,name='category'),
]
