from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    post = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts":post})
    # print(posts[0].title)
    # return render(request, "blog/post_list.html")
    
def post_like(request):
    print('LIKE')
    if request.method == 'POST':
        post.id = request.POST.get('post_id')
        post = Post.objects.get(id = post_id)
        post.save()
    return redirect("post_list")