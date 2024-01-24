from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404("Nie znaleziono posta.")
    
    # post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, publish__year=year, publish__month=month, publish__day=day, slug=post)
    
    return render(request, 'blog/post/detail.html', {'post': post})