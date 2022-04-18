from django.shortcuts import redirect, HttpResponse, render, get_object_or_404
from .models import Blog, Tag, Category, About
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, TemplateView, DetailView
try:
    from urllib.parse import quote_plus
except:
    pass
from django.db.models import Count, Q
from django.core.paginator import Paginator
# from .forms import CommentForm

# Create your views here.


def allblogs(request, category_slug=None, tag_slug=None):
    category = None
    tagger = None
    bloglist = Blog.objects.filter(draft=False)
    blog_filter = bloglist.order_by('published_date')
    about = About.objects.all()
    categorylist = Category.objects.annotate(total_category=Count('blog'))
    taglist = Tag.objects.annotate(total_tag=Count('blog'))

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        bloglist = bloglist.filter(category=category)
    # the following checks if the category and tag slug is selected and filters the result
    if tag_slug:
        tagger = Tag.objects.get(slug=tag_slug)
        bloglist = bloglist.filter(tag=tagger)
    # the following handles pagination
    paginator = Paginator(bloglist, 10)  # shows s-ecifoc number of posts
    page = request.GET.get('page')
    bloglist = paginator.get_page(page)

    context = {
        'bloglist': bloglist,
        'categ': categorylist,
        'tag': taglist,
        'about': about,
        'blog_filter': blog_filter,
    }
    template = 'blog/blog.html'
    return render(request, template, context)


# the following manages the blog blog_details
def blogdetails(request, slug=None):
    detailblog = get_object_or_404(Blog, slug=slug)
    allblogs = Blog.objects.all()
    categories = Category.objects.annotate(total_category=Count('blog'))
    tagger = Tag.objects.annotate(total_tag=Count('blog'))
    share_string = quote_plus(detailblog.content)

    # the following handles pagination
    page = request.GET.get('page')
    template = 'blog/single.html'
    context = {'blog': detailblog,
               'allblog': allblogs,
               'category': categories,
               'tagger': tagger,
               'share_string': share_string,
               }
    return render(request, template, context)


class SearchListView(ListView):
    model = Blog
    template_name = "blog/blog.html"

    def get_query_set(self):
        # this is for blog search\
        search_query = self.request.GET.get('q')
        if search_query:
            blogging = self.model.objects.filter(
                Q(title__icontains=search_query) | Q(
                    content__icontains=search_query)
                | Q(category__types__icontains=search_query) | Q(tag__types__icontains=search_query)
            ).distinct()
        else:
            blogging = self.model.objects.none()
        return blogging


# @login_required
# def comment(request, slug):
#     blog = get_object_or_404(Blog, slug)
#     if request.method == 'POST':
#         form = CommentForm(request.POST or None)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog_comment = blog
#             comment.save()
#         # redirect ('blog_details', slug=blog.slug)
#         return redirect('blog.get_absolute_url')
#     else:
#         commentform = CommentForm()
#     template = 'blog/single.html'
#     context = {'commentform': commentform}
#     return render(request, template, context)


def contact(request):
    return render(request, 'contact.html')
