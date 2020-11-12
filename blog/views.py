from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    template_name = 'blog/blog.html'
    context = {
        'blogs': blogs
    }
    return render(request, template_name, context)


def texto(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog
    }
    template_name = 'blog/texto.html'

    return render(request, template_name, context)
