from django.shortcuts import render
from .models import *
from blog.models import Blog

def index(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    blogs = Blog.objects.all()
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'blogs':blogs,
    }
    return render(request,'index.html',context)


def about(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    about = About.objects.all()
    par = About_paragraph.objects.all()
    context = {
        'i':i,
        'em':em,
        'ph':ph,
        'about':about,
        'par':par,
    }
    return render(request,'about.html',context)

def portfolio(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    about = About.objects.all()
    por = Portfolio.objects.all()
    context = {
        'i':i,
        'em':em,
        'ph':ph,
        'about':about,
        'por':por,
    }
    return render(request,'portfolio.html',context)