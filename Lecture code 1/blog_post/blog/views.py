from django.shortcuts import render, redirect
from blog.models import BlogPost


def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})


def blog_post_detail(request, pk):
    blog = BlogPost.objects.filter(pk=pk).first()
    if not blog:
        return redirect('not_found')
    return render(request, 'blog_detail.html', context={'blog': blog})


def not_found(request):
    return render(request, template_name='404.html')