"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import magic_number
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list
from playlist import views
from blog.views import post_like
from core.views import mysite

urlpatterns = [
    path('admin/', admin.site.urls),
    path("magic_number/", magic_number),
    path("blog/posts_list/", post_list, name = 'post_list'),
    path('playlist/video_list/', views.video_list, name = 'video_list'),
    path("playlist/video_create/", views.video_create, name = 'video_create'),
    path(" blog/post_like/", post_like, name = 'post_like'),
    path("core/mysite/", mysite, name = "mysite"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)