from django.urls import path
from .views import *


urlpatterns = [
    path('staff/',staff,name="staff"),
]
