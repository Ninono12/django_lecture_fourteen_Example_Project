from django.urls import path
from blog.views import (
    not_found,
    blog_post_list,
    blog_post_detail,
    blog_post_create,
    blog_post_update,
    blog_post_delete
)

urlpatterns = [
    path('not_found/', not_found, name='not_found'),
    path('blog_post_list/', blog_post_list, name='blog_post_list'),
    path('blog_post_detail/<int:pk>/', blog_post_detail, name='blog_post_detail'),
    path('blog_post_create/', blog_post_create, name='blog_post_create'),
    path('blog_post_update/<int:pk>/', blog_post_update, name='blog_post_update'),
    path('blog_post_delete/<int:pk>/', blog_post_delete, name='blog_post_delete'),
]