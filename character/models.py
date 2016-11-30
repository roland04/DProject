from django.db import models
from django.contrib.auth.models import User
from universe.models import Planet

class Character(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currentposition = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
