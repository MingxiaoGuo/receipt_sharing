from django.db import models

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=64)
    recipe_description = models.CharField(max_length=512)