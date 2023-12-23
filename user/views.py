from django.shortcuts import render
from .models import *


def staff(request):
    return render(request,'staff.html')