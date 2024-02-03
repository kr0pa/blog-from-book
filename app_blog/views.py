from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/post/list.html'
    paginate_by = 3

# Create your views here.
# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
    
#     return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404("Nie znaleziono posta.")
    
    # post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, publish__year=year, publish__month=month, publish__day=day, slug=post)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'form': form})


def post_share(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    sent = False
    
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} zalecia Ci przeczytanie {post.title}"
            message = f"Przeczytaj {post.title} pod adresem {post_url}\n\n komentarze {cd['name']}: {cd['comments']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})