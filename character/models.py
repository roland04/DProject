from django.db import models
from django.contrib.auth.models import User
from universe.models import Planet

class Attribute(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, default=" ")
    attribute = models.ForeignKey(Attribute)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    max_hitpoints = models.IntegerField(default=100)
    current_hitpoints = models.IntegerField(default=0)
    fame = models.IntegerField(default=0)
    currentposition = models.ForeignKey(Planet, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(Attribute, through='CharacterAttribute')
    skills = models.ManyToManyField(Skill, through='CharacterSkill')

    def __str__(self):
        return self.name

class CharacterSkill(models.Model):
    character = models.ForeignKey(Character)
    skill = models.ForeignKey(Skill)
    value = models.IntegerField(default=0)

    def __str__(self):
        return "%s(%s)" % (self.character.name, self.skill.name)

class CharacterAttribute(models.Model):
    character = models.ForeignKey(Character)
    attribute = models.ForeignKey(Attribute)
    value = models.IntegerField(default=0)

    def __str__(self):
        return "%s(%s)" % (self.character.name, self.attribute.name)

class ShipModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=20)
    shipmodel = models.ForeignKey(ShipModel)

    def __str__(self):
        return self.name
