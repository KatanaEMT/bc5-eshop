from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def homepage(request):
    # SELECT * FROM Product;
    product_list = Product.objects.all()
    
    context = {"products": product_list}
    
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html', context)
