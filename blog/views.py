from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    template_name = 'blog/blog.html'
    context = {
        'blogs': blogs
    }
    return render(request, template_name, context)


def texto(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    template_name = 'blog/texto.html'

    return render(request, template_name, context)
