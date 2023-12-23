from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Idata(models.Model):
    name = models.CharField(max_length=255)
    extend = models.CharField(max_length=255)
    motto = models.CharField(max_length=255)

    logo = models.ImageField(upload_to='website/logo')

    copyright = models.BooleanField(default=False)

    twitter = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    

class Email(models.Model):
    to = models.ForeignKey(Idata,on_delete=models.CASCADE)
    address = models.EmailField()

class Phone(models.Model):
    to = models.ForeignKey(Idata,on_delete=models.CASCADE)
    number = PhoneNumberField()

class About(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    

class About_paragraph(models.Model):
    to = models.ForeignKey(About,on_delete=models.CASCADE)
    paragraph = models.TextField(max_length=2000)


class Newsettler(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='protfolio')
    name = models.CharField(max_length=255,null=True)
    link = models.URLField(null=True)
    disc = models.TextField(max_length=2000)
    def __str__(self):
        return self.name
