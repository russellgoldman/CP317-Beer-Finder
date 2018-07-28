from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Beer, ContainerType, Taste, Brand
import django
from . import models
#from django.core.context_processors import csrf
# Create your views here.

def home(request):
    return render(request, "home/home page.html")
def login_page(request):
    return render(request, "home/login.html")
def signup_page(request):
    return render(request, "home/signup.html")
def contact_page(request):
    return render(request, "home/contact.html")
def about_page(request):
    return render(request, "home/about.html")
def article_page(request):
    return render(request, "home/article page.html")

def top_picks(request):
    return render(request, "home/top picks.html")

def product_page(request, name):
    # beer = Beer.objects.order_by('beerName')
    beer = Beer.objects.filter(beerName=name)
    beer_dict = {'item': beer[0]}
    return render(request, "home/product page.html", context=beer_dict)

def library_page(request):
    beer_list = Beer.objects.order_by('beerName')
    query = request.GET.get("type")
    if query:
        beer_list = Beer.objects.filter(containerType__containerTypeName=query)



    beer_dict = {'library_page':beer_list}
    return render(request, "home/library page.html", context=beer_dict)

def form_view(request):
    # form =forms.NewBeer()
    form = forms.NewBeer(request.POST, request.FILES)
    # form = forms.FormName()

    if request.method == 'POST':
        form = forms.NewBeer(request.POST, request.FILES)

        if form.is_valid():

            #add form to data base, do something

            beer_name = form.cleaned_data['beerName']
            photo = form.cleaned_data['beerPhoto']
            acl = form.cleaned_data['alcoholVolume']
            can_Price = form.cleaned_data['canPrice']
            bottle_Price = form.cleaned_data['bottlePrice']
            keg_Price = form.cleaned_data['kegPrice']
            brand_a = form.cleaned_data['brand']
            body_Type = form.cleaned_data['bodyType']
            container_Type = form.cleaned_data['containerType']
            taste_a = form.cleaned_data['taste']

            new_beer = Beer(beerName=beer_name,beerPhoto=photo, alcoholVolume=acl, canPrice=can_Price,bottlePrice=bottle_Price,kegPrice=keg_Price,brand=brand_a, bodyType = body_Type)
            new_beer.save()
            for container in container_Type:
                new_beer.containerType.add(container)
                new_beer.save()
            for t in taste_a:
                new_beer.taste.add(t)
                new_beer.save()
            print("Validation success!")
            # redirect, i want to update this so that it goes to the beer lists page later
            return HttpResponse("Beer added. Thank you")
    else:
        form = forms.NewBeer()
    return render(request, 'home/add beer.html', {'form':form})

def filter_form_view(request):
    form = forms.SearchBeer(request.POST)


    if request.method == 'POST':
        if form.is_valid():

            #add form to data base, do something
            acl = form.cleaned_data['alcoholVolume']
            brand_a = form.cleaned_data['brand']
            body_Type = form.cleaned_data['bodyType']
            container_Type = form.cleaned_data['containerType']
            taste_a = form.cleaned_data['taste']

            beer_list = Beer.objects.filter(alcoholVolume=acl, brand__brandName=brand_a, bodyType__bodyTypeName=body_Type, containerType__in=container_Type, taste__in=taste_a)
            print(beer_list)
            return render(request, 'home/results.html', {'beerList':beer_list})
    else:
        form = forms.SearchBeer()

    return render(request, 'home/filter page.html', {'form':form})

def results(request):
    return render(request, 'home/results.html')