from django.contrib import admin
from .models import *


admin.site.register(Blog_Post)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)