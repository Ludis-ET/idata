from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "idata administration"
admin.site.name = "idata"
urlpatterns = [
    path('admin-ludis/', admin.site.urls),
    path('',include('core.urls')),
    path('blog/',include('blog.urls')),
    path('course/',include('course.urls')),
    path('users/',include('user.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)