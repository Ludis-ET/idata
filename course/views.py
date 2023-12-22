from django.shortcuts import render,redirect
from .models import *
from core.models import *
from django.contrib import messages

def course(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    courses = Course.objects.all()
    categories = Category.objects.all()
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'courses':courses,
        'categories':categories,
    }
    return render(request,'course.html',context)