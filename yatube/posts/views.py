from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.select_related()[:10]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related()[:10]
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'group': group,
        'posts': posts,
        'title': title

    }
    return render(request, 'posts/group_list.html', context, )
