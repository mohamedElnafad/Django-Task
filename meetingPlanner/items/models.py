from django.db import models

# Create your models here.
class Itmes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)


class NewProduct(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Image = models.CharField(max_length=200)