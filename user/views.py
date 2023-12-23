from django.shortcuts import render
from .models import *
from core.models import *


def staff(request):
    i = Idata.objects.get(id=1)
    em = Email.objects.all()
    ph = Phone.objects.all()
    staffs = Staff.objects.all()
    context ={
        'i':i,
        'em':em,
        'ph':ph,
        'staffs':staffs,
    }
    return render(request,'staff.html',context)