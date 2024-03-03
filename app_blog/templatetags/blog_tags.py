from django import template
from app_blog.models import Post

register = template.Library()

@register.simple_tag(name='all_posts')
def total_post():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status='PB').order_by('-publish')[:count]
    return {'latest_posts': latest_posts}