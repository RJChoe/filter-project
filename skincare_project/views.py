from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to the Skincare Home Page!")
    return render(request, 'home.html')
    

def product(request):
    #return HttpResponse("Product Ingredient Input Page")
    return render(request, 'product.html')

