from django.shortcuts import render,redirect
from .models import *
from blog.models import Blog
from course.models import Course
from user.models import Staff,Comment
from django.contrib import messages

def index(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    blogs = Blog.objects.all()
    courses = Course.objects.all()
    staffs = Staff.objects.all()
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'blogs':blogs,
        'courses':courses,
        'staffs':staffs,
    }
    return render(request,'index.html',context)


def about(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    about = About.objects.all()
    par = About_paragraph.objects.all()
    staffs = Staff.objects.all()
    context = {
        'i':i,
        'em':em,
        'ph':ph,
        'about':about,
        'par':par,
        'staffs':staffs,
    }
    return render(request,'about.html',context)


def contact(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    if request.method == 'POST':
        a = request.POST['message']
        b = request.POST['name']
        c = request.POST['email']
        Comment.objects.create(name=c,email=b,text=a)
        messages.success(request,'message succesfully transfered thankyou for your interest.')
        return redirect('contact')

    context = {
        'i':i,
        'em':em,
        'ph':ph,
    }
    return render(request,'contact.html',context)

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