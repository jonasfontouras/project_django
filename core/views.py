from django.shortcuts import render
from .models import Product


# Create your views here.
def ayurveda_site(request):
    products = Product.objects.all()
    template_name = 'index.html'
    context = {
        'products': products
    }
    return render(request, template_name, context)

