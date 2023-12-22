from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    #count = models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='blog/poster')
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True)
    date = models.DateField(auto_now_add=True)
    disc = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Blog_Post(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    paragraph = models.TextField(max_length=5555)
    important = models.BooleanField(default=False)

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        self.name