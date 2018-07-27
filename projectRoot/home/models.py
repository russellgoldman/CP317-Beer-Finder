from django.db import models
from datetime import datetime


# tables pointed to by Beer with many-to-one relationship:

class Brand(models.Model):
    brandName = models.CharField(max_length=50)
    countryOfOrigin = models.CharField(max_length=50)

    def __str__(self):
        return self.brandName


class BodyType(models.Model):
    bodyTypeName = models.CharField(max_length=20)

    def __str__(self):
        return self.bodyTypeName


class Colour(models.Model):
    colourNum = models.IntegerField(default=0)
    colourHex = models.CharField(max_length=10)

    def __str__(self):
        return str(self.colourNum)


# tables pointed to by Beer with many-to-many relationship:

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
    beerPhoto = models.ImageField(upload_to='beers')
    alcoholVolume = models.FloatField(default=0.0)
    canPrice = models.FloatField(default=0.0)
    bottlePrice = models.FloatField(default=0.0)
    kegPrice = models.FloatField(default=0.0)

    # reference to the Brand model (many-to-one),
    # if the Brand is deleted so will the Beer, thus on_delete=models.CASCADE,
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # reference to the BodyType model (many-to-one)
    # if the BodyType is deleted so will the Beer, thus on_delete=models.CASCADE
    bodyType = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    # reference to the Colour model (many-to-one)
    # if the Colour is deleted so will the Beer, thus on_delete=models.CASCADE
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)

    # reference to the ContainerType model (many-to-many)
    containerType = models.ManyToManyField(ContainerType)
    # reference to the Taste model (many-to-many)
    taste = models.ManyToManyField(Taste)

    def __str__(self):
        return self.beerName


# tables that point to Beer with many-to-one relationship:

class Rating(models.Model):
    ratingValue = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    reviewText = models.TextField()
    # reference to the Beer model (one-to-one),
    # if the Beer is deleted so will the Rating, thus on_delete=models.CASCADE,
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ratingValue)
