from django.db import models

class Star(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")

    def __str__(self):
        return self.name

class Faction(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    star = models.ForeignKey(Star, on_delete=models.CASCADE)

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

class Moon(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

class LocationType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")

class Location(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    locationtype = models.ForeignKey(LocationType)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")
    resources = models.ManyToManyField(Resource, through='ItemResource')

    def __str__(self):
        return self.name

class ItemResource(models.Model):
    item = models.ForeignKey(Item)
    resource = models.ForeignKey(Resource)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "%s(%s)" % (self.item.name, self.resource.name)
