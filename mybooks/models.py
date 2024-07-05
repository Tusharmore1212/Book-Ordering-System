from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img')
    file = models.FileField(upload_to='static/img/files/', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

class Buyerinfo(models.Model):
    cname = models.CharField(max_length=255)
    cemail = models.EmailField(max_length=255)
    cphone = models.CharField(max_length=10)
    cadd = models.CharField(max_length=255)
    bname = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    totalamout = models.PositiveIntegerField()

    

