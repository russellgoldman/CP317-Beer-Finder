from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Beer, Rating
import django
from . import models
from home.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg

#from django.core.context_processors import csrf
# Create your views here.

def home(request):
    return render(request, "home/home page.html")
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                HttpResponse("Account not active!")
        else:
            print("someone tried to login and failed!")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details")
    else:

        return render(request, 'home/login.html', {})
    # return render(request, "home/login.html")
def signup_page(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'home/signup.html', {'user_form': user_form, 'registered': registered})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))
def contact_page(request):
    return render(request, "home/contact.html")
def about_page(request):
    return render(request, "home/about.html")
def article_page(request):
    return render(request, "home/article page.html")

def top_picks(request):
    # get list of beers
    beers = Beer.objects.all()

    # create 2D list with inner lists consisting of [beer, average rating]
    beers_ratings = []
    for i in range(len(beers)):
        inner_list = []
        inner_list.append(beers[i])
        rating_dict = Rating.objects.filter(beer__beerName = beers[i]).aggregate(Avg("ratingValue"))
        if rating_dict['ratingValue__avg'] is None:
            inner_list.append(0)
        else:
            inner_list.append(rating_dict['ratingValue__avg'])
        beers_ratings.append(inner_list)

    # sort 2D list using insertion sort for efficiency
    n = len(beers_ratings)
    for i in range(1, n):
        save = beers_ratings[i]
        j = i
        while j > 0 and beers_ratings[j-1][1] > save[1]:
            beers_ratings[j] = beers_ratings[j-1]
            j -= 1
            beers_ratings[j] = save

    # create final list of sorted beers
    beer_list = []
    for i in range(len(beers_ratings)):
        beer_pair = beers_ratings.pop(-1)
        beer_list.append(beer_pair[0])

    return render(request, "home/top picks.html", {'beerList': enumerate(beer_list, start=1)})

def product_page(request, name):
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
@login_required(login_url='/login/')
def form_view(request):

    form = forms.NewBeer(request.POST, request.FILES)

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

            beerlst = Beer.objects.filter(alcoholVolume=acl, brand__brandName=brand_a, bodyType__bodyTypeName=body_Type, containerType__in=container_Type, taste__in=taste_a)

            beer_list = []

            for beer in beerlst:
                if beer not in beer_list:
                    beer_list.append(beer)
            return render(request, 'home/results.html', {'beerList': beer_list})
    else:
        form = forms.SearchBeer()

    return render(request, 'home/filter page.html', {'form':form})

def results(request):
    return render(request, 'home/results.html')