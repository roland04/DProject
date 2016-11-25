from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

    TINY = 'TY'
    SMALL = 'SM'
    MEDIUM = 'ME'
    LARGE = 'LA'
    COLOSSAL = 'CO'
    PLANET_SIZES_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (COLOSSAL, 'Colossal'),
    )
    size = models.CharField(
        max_length=20,
        choices=PLANET_SIZES_CHOICES,
        default=MEDIUM,
    )

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    HANGAR = 'HA'
    CANTINA = 'CA'
    MARKET = 'MA'
    QUEST = 'QU'
    LOCATION_TYPE_CHOICES = (
        (HANGAR, 'Hangar'),
        (CANTINA, 'Cantina'),
        (MARKET, 'Market'),
        (QUEST, 'Quest'),
    )
    locationtype = models.CharField(
        max_length=20,
        choices=LOCATION_TYPE_CHOICES,
    )

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.name
