from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    cl = models.CharField(max_length=100,null=True,unique=True)
    def __str__(self):
        return self.name
    
c = [
    ('year','year'),
    ('month','month'),
    ('once','once'),
]
class Course(models.Model):
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,blank=True)
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='course/poster')
    rating = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(default=0)
    per = models.CharField(choices=c,max_length=255,blank=True)
    disc = models.TextField(max_length=1000,null=True)
    r1 = models.IntegerField(blank=True,default=0)
    r15 = models.IntegerField(blank=True,default=0)
    r2 = models.IntegerField(blank=True,default=0)
    r25 = models.IntegerField(blank=True,default=0)
    r3 = models.IntegerField(blank=True,default=0)
    r35 = models.IntegerField(blank=True,default=0)
    r4 = models.IntegerField(blank=True,default=0)
    r45 = models.IntegerField(blank=True,default=0)
    r5 = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name
