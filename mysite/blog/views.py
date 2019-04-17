from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    # Use a specific QuerySet instead of retrieving all objects.
    # Instead of defining a queryset attribute, we could have
    # specified model = Post and Django would have built the generic
    # Post.objects.all() QuerySet for us
    queryset = Post.published.all()
    # Use the context variable posts for the query results. The default variable is object_list
    # if we don't specify any context_object_name.
    context_object_name = 'posts'
    # Paginate the result displaying three objects per page.
    paginate_by = 3
    # Use a custom template to render the page. If we don't set a
    # default template, ListView will use blog/post_list.html.
    template_name = 'blog/post/list.html'


def post_list(request):
    """
    In this view, we are retrieving all the posts
    with the published status using the published manager we created
    previously
    :param request:
    :return:
    """
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 分页功能，每页 3篇文章
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    """
    This is the post detail view. This view takes year, month, day, and post
    parameters to retrieve a published post with the given slug and date.
    Note that when we created the Post model, we added the
    unique_for_date parameter to the slug field. This way, we ensure that
    there will be only one post with a slug for a given date, and thus, we
    can retrieve single posts using date and slug.
    :param request:
    :param year:
    :param month:
    :param day:
    :param post:
    :return:
    """
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
