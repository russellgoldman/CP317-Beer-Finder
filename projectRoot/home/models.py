from django.db import models

# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class BodyType(models.Model):
    body_type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.body_type_name


class Beer(models.Model):
    beer_name = models.CharField(max_length=50)
    colour_srm_value = models.FloatField(default=0.0)
    alcohol_by_volume = models.FloatField(default=0.0)
    # reference to the Brand model (one-to-many, i.e. One Brand associated with One to Many Beers)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # reference to the BodyType model (one-to-many)
    # null=True to allow for Beer that has no BodyType matched to it yet
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.beer_name


class Taste(models.Model):
    taste_name = models.CharField(max_length=50)
    # reference to the Beer model (many-to-many)
    # blank=True to allow for Taste that has no Beer matched to it yet
    beer = models.ManyToManyField(Beer, blank=True)

    def __str__(self):
        return self.taste_name


class ContainerStyle(models.Model):
    container_style_name = models.CharField(max_length=20)
    # reference to the Beer model (many-to-many)
    # blank=True to allow for ContainerStyle that has no Beer matched to it yet
    beer = models.ManyToManyField(Beer, blank=True)

    def __str__(self):
        return self.container_style_name
