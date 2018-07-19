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

def article_page(request):
    return render(request, "home/article page.html")

def top_picks(request):
    return render(request, "home/top picks.html")

def product_page(request):
    return render(request, "home/product page.html")

def filter_page(request):
    return render(request, "home/filter page.html")

def library_page(request):
    beer_list = Beer.objects.order_by('beerName')
    beer_dict = {'library_page':beer_list}
    return render(request, "home/library page.html", context=beer_dict)
def add_beer(request):
    return render(request, "home/add beer.html")
def form_view(request):
    form =forms.NewBeer()

    # form = forms.FormName()

    if request.method == 'POST':
        form = forms.NewBeer(request.POST)

        if form.is_valid():

            #add form to data base, do something

            beer_name = form.cleaned_data['beerName']
            colour_Hex = form.cleaned_data['colourHex']
            acl = form.cleaned_data['alcoholVolume']
            can_Price = form.cleaned_data['canPrice']
            bottle_Price = form.cleaned_data['bottlePrice']
            keg_Price = form.cleaned_data['kegPrice']
            brand_a = form.cleaned_data['brand']
            body_Type = form.cleaned_data['bodyType']
            container_Type = form.cleaned_data['containerType']
            taste_a = form.cleaned_data['taste']

            new_beer = Beer(beerName=beer_name,colourHex=colour_Hex, alcoholVolume=acl, canPrice=can_Price,bottlePrice=bottle_Price,kegPrice=keg_Price,brand=brand_a, bodyType = body_Type)
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