from django.db import models

# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class Beer(models.Model):
    beer_name = models.CharField(max_length=50)
    colour = models.IntegerField()
    alcohol_percentage = models.FloatField()
    body = models.CharField(max_length=50)
    # reference to the Brand model (one-to-one)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.beer_name


class TasteOptions(models.Model):
    taste_option_name = models.CharField(max_length=50)
    # reference to the Beer model (many-to-many)
    beer = models.ManyToManyField(Beer)

    def __str__(self):
        return self.taste_option_name


class ContainerOptions(models.Model):
    container_option_name = models.CharField(max_length=20)
    # reference to the Beer model (many-to-many)
    beer = models.ManyToManyField(Beer)

    def __str__(self):
        return self.container_option_name
