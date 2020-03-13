from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Blog, Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.blog = Blog.objects.get(author=self.request.user)
        obj.save()
        return super(PostCreateView, self).form_valid(form)


class PostListView(ListView):
    model = Post

    def get_queryset(self, **kwargs):
        user = self.kwargs['user']
        if user:
            blog = Blog.objects.get(author=user)
        else:
            blog = Blog.objects.get(author=self.request.user)
        return Post.objects.filter(blog=blog)


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
