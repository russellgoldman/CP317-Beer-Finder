from django.db import models
from datetime import datetime


class Brand(models.Model):
    brandName = models.CharField(max_length=50)
    countryOfOrigin = models.CharField(max_length=50)

    def __str__(self):
        return self.brandName


class Colour(models.Model):
    colourNum = models.IntegerField(default=0)
    colourHex = models.CharField(max_length=10)

    def __str__(self):
        return str(self.colourNum)


class BodyType(models.Model):
    bodyTypeName = models.CharField(max_length=20)

    def __str__(self):
        return self.bodyTypeName


class ContainerType(models.Model):
    containerTypeName = models.CharField(max_length=20)

    def __str__(self):
        return self.containerTypeName


class Taste(models.Model):
    tasteName = models.CharField(max_length=50)

    def __str__(self):
        return self.tasteName


class Beer(models.Model):
    beerName = models.CharField(max_length=50)
    beerPhoto = models.ImageField(upload_to='beers', blank=True)
    alcoholVolume = models.FloatField(default=0.0)
    canPrice = models.FloatField(default=0.0, blank=True, null=True)
    bottlePrice = models.FloatField(default=0.0, blank=True, null=True)
    kegPrice = models.FloatField(default=0.0, blank=True, null=True)
    # reference to the Brand model (many-to-one)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # reference to the BodyType model (many-to-one)
    # null=True to allow for Beer that has no BodyType matched to it yet
    bodyType = models.ForeignKey(BodyType, on_delete=models.CASCADE, null=True)
    # reference to the Colour model (many-to-one)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, null=True)
    # reference to the ContainerType model (many-to-many)
    # blank=True to allow for Beer that has no ContainerType matched to it yet
    containerType = models.ManyToManyField(ContainerType, blank=True)
    # reference to the Taste model (many-to-many)
    taste = models.ManyToManyField(Taste, blank=True)

    def __str__(self):
        return self.beerName


class Rating(models.Model):
    ratingValue = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)
    reviewText = models.TextField(blank=True, null=True)
    # reference to the Beer model (one-to-one)
    # null=True to allow for Beer without Rating
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.ratingValue)
