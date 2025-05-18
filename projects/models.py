from django.db import models

# Create your models here.
class Teams(models.Model):
    nombre = models.CharField(max_length=100)
    logo_name = models.CharField(max_length=100)

class Categories(models.Model):
    categoria = models.CharField(max_length=5)

class CategoriesInfo(models.Model):
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    id_team = models.ForeignKey(Teams, on_delete=models.CASCADE)