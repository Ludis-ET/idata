from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('about-us/',about,name='about'),
    path('portfolio/',portfolio,name='portfolio'),
    path('contact-us/',contact,name='contact'),
]
