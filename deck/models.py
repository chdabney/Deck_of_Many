from contextlib import nullcontext
from django.db import models

# Create your models here.
class Deck(models.Model):
     pass

class Card(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    card_image = models.ImageField(null=False)