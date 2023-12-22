from django.shortcuts import render,redirect
from .models import *
from core.models import *
from django.contrib import messages

def blog(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'blogs':blogs,
        'categories':categories,
    }
    return render(request,'blog.html',context)

def newsettler(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        em = request.POST['email']
        Newsettler.objects.create(email=em)
        messages.success(request,'successfully registered!')
        return redirect('blog')
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'blogs':blogs,
        'categories':categories,
    }
    return render(request,'blog.html',context)

def category(request,id):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    cat = Category.objects.get(id=id)
    blogs = Blog.objects.filter(category=cat)
    categories = Category.objects.all()
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'blogs':blogs,
        'categories':categories,
        'cat':cat,
    }
    return render(request,'category.html',context)

def search(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        str = request.POST['search']
        blogs = Blog.objects.filter(name__icontains = str)
        context ={
            'i':i,
            'em':em,
            'ph':ph,
            'blogs':blogs,
            'categories':categories,
            'str':str,
        }
        return render(request,'search.html',context)
    

def blog_post(request,id):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    blog = Blog.objects.get(id=id)
    posts = Blog_Post.objects.filter(blog=blog)
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    before = blogs.get(id=(blog.id - 1)) if blogs.filter(id = (blog.id -1)).exists() else False
    after = blogs.get(id=(blog.id + 1)) if blogs.filter(id = (blog.id + 1)).exists() else False
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['comment']
        Comment.objects.create(blog=blog,name=a,email=b,comment=c)
        messages.success(request,'comment sucessfully posted.')
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'blog':blog,
        'posts':posts,
        'blogs':blogs,
        'categories':categories,
        'before':before,
        'after':after,
        'comments':comments,
    }
    return render(request,'post.html',context)