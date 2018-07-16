from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/home page.html")

def article_page(request):
    return render(request, "home/article page.html")

def top_picks(request):
    return render(request, "home/top picks.html")

def product_page(request):
    return render(request, "home/product page.html")

def filter_page(request):
    return render(request, "home/filter page.html")

def library_page(request):
    return render(request, "home/library page.html")