from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


def post_list(request):
    context = {
        "posts": Post.published.all()
    }
    return render(request, template_name="list.html", context=context)


def post_detail(request, year, month, day, post):
    context = {
        "post": get_object_or_404(Post,
                                  slug=post,
                                  status='published',
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day)
    }
    return render(request, "detail.html", context=context)