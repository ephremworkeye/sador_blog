from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post})