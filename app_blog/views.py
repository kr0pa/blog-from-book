from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404("Nie znaleziono posta.")
    
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/detail.html', {'post': post})