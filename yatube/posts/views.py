from django.shortcuts import get_object_or_404, render

from yatube.settings import NUMBER_OF_ENTRIES

from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:NUMBER_OF_ENTRIES]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author').all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context, )
