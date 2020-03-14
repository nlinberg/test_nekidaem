from django.urls import path
from .views import PostDetailView, PostCreateView, PostListView, BlogListView, BlogFollowRedirectView, FeedListView

urlpatterns = [
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/list/<int:user>/', PostListView.as_view(), name='post-list'),
    path('follow/<int:blog>/', BlogFollowRedirectView.as_view(), name='blog-follow'),
    path('list/', BlogListView.as_view(), name='blog-list'),
    path('feed/', FeedListView.as_view(), name='feed-list'),
]
