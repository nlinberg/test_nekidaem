from django.urls import path
from .views import PostDetailView, PostCreateView, PostListView, BlogListView

urlpatterns = [
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/list/<int:user>/', PostListView.as_view(), name='post-list'),
    path('list/', BlogListView.as_view(), name='blog-list'),
]