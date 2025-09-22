from urllib import request

from django.db.models.fields import return_None
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import BlogPostModelForm
from blog.models import BlogPost, BannerImage



def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})


def blog_post_detail(request, pk):
    blog = get_object_or_404(
        BlogPost.objects.prefetch_related('images').select_related('banner_image'),
        pk=pk
    )
    return render(request, template_name='blog_detail.html', context={'blog': blog})


def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            banner_image = form.cleaned_data.get('banner_image')
            if banner_image:
                BannerImage.objects.create(blog_post=blog_post, image=banner_image)
            return redirect('blog_post_list')
    else:
        form = BlogPostModelForm()

    return render(request, template_name='blog_create.html', context={'form': form})
def blog_post_update(request, pk):
    blog = BlogPost.objects.filter(pk=pk).first()
    if not blog:
        return redirect('not_found')

    if request.method == 'POST':
        form = UpdateBlogPostModelForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', pk=blog.pk)  # Redirect to the detail page
    else:
        form = UpdateBlogPostModelForm(instance=blog)  # Pre-fill the form with existing data

    return render(request, 'blog_update.html', {'form': form})

def not_found(request):
    return render(request, template_name='404.html')

def blog_post_delete(request, pk):
    blog = BlogPost.objects.filter(id=pk).first()
    if not blog:
        return redirect('blog_post_list')

    if request.method == 'POST':
        blog.deleted = True  # ან blog.delete()
        blog.save()
        return redirect('blog_post_list')

    return render(request, template_name='blog_post_confirm_delete.html', context={'blog': blog})