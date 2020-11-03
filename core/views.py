from django.shortcuts import render


# Create your views here.

def ayurveda_site(request):
    return render(request, 'index.html')
