from django.shortcuts import render
from .models import Course


# Create your views here.
def courses(request):
    courses = Course.objects.all()
    template_name = 'courses/courses.html'
    context = {
        'courses': courses
    }

    return render(request, template_name, context)


def details(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'course': course
    }
    template_name = 'courses/details.html   '
    return render(request, template_name, context)
