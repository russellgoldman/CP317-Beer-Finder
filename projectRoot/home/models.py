from django.db import models

# Create your models here.


class Brand(models.Model):
    brandName = models.CharField(max_length=50)
    countryOfOrigin = models.CharField(max_length=50)

    def __str__(self):
        return self.brandName


class BodyType(models.Model):
    bodyTypeName = models.CharField(max_length=20)

    def __str__(self):
        return self.bodyTypeName


class Beer(models.Model):
    beerName = models.CharField(max_length=50)
    colourValue = models.FloatField(default=0.0)
    alcoholVolume = models.FloatField(default=0.0)
    # reference to the Brand model (many-to-one)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # reference to the BodyType model (many-to-one)
    # null=True to allow for Beer that has no BodyType matched to it yet
    bodyType = models.ForeignKey(BodyType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.beerName


class Taste(models.Model):
    tasteName = models.CharField(max_length=50)
    # reference to the Beer model (many-to-many)
    # blank=True to allow for Taste that has no Beer matched to it yet
    beer = models.ManyToManyField(Beer, blank=True)

    def __str__(self):
        return self.tasteName


class ContainerType(models.Model):
    containerTypeName = models.CharField(max_length=20)
    # reference to the Beer model (many-to-many)
    # blank=True to allow for ContainerStyle that has no Beer matched to it yet
    beer = models.ManyToManyField(Beer, blank=True)

    def __str__(self):
        return self.container_style_name


class Rating(models.Model):
    ratingValue = models.IntegerField(default=0)
    authorName = models.CharField(max_length=50)
    # reference to the Beer model (one-to-one)
    # null=True to allow for Beer without Rating
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ratingValue
