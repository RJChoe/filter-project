from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Skincare Home Page!")

def user(request):
    return HttpResponse("User Allergy Input Page")

def product(request):
    return HttpResponse("Product Ingredient Input Page")

