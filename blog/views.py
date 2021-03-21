from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import BlogCommentForm
from .models import Blog, BlogAuthor, BlogComment

# Create your views here.
def index(request):
    """ Home page """
    context = {}
    return render(request, 'blog/index.html', context=context)


class BlogListView(generic.ListView):
    """ List of all blog posts """
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    """ Blog post detail page """
    model = Blog


class BloggerListView(generic.ListView):
    """ List of all bloggers """
    model = BlogAuthor


class BloggerDetailView(generic.DetailView):
    """ Blog author (blogger) detail page """
    model = BlogAuthor


def create_blog_comment(request, pk):
    """ Comment form page """
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            blog_comment = BlogComment()
            blog_comment.blog = blog
            blog_comment.author = request.user
            blog_comment.description = form.cleaned_data['description']
            blog_comment.save()

            return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': blog.pk}))

    else:
        form = BlogCommentForm()
    
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/blog_comment_form.html', context)

