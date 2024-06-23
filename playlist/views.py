from django.shortcuts import render, redirect

# Create your views here.

from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'playlist/video_list.html', {"videos": videos})


def video_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        embed_code = request.POST.get("embed_code")
        Video.objects.create(
            title = title, 
            embed_code = embed_code,)
        return redirect('video_list')
    return render(request, "playlist/video_create.html")