from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='user/staff/')
    pro = models.CharField(max_length=255)
    def __str__(self):
        return self.name
