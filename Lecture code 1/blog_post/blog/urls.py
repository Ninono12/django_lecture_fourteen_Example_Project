from django.urls import path
from blog.views import not_found, blog_post_list, blog_post_detail

urlpatterns = [
    path('not_found/', not_found, name='not_found'),
    path('blog_post_list/', blog_post_list, name='blog_post_list'),
    path('blog_post_detail/<int:pk>/', blog_post_detail, name='blog_post_detail'),
]
