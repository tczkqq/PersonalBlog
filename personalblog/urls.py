from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "PersonalBlog"

urlpatterns = [
    path('', include('blog.urls'), name='blog'),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
