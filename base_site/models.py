from django.db import models
from autoslug import AutoSlugField

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("base_site:detail", kwargs={"slug": self.slug})

class Pedido(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    qnt = models.IntegerField()
    product_price = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


