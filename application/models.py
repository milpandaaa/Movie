from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    photo = models.TextField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Сassette(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    year = models.IntegerField()
    theme = models.CharField(max_length=50)
    duration = models.TimeField()
    film_studio = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    poster = models.TextField()


class Seller(models.Model):
    address = models.CharField(max_length=50)


class Selling(models.Model):
    id_cassette = models.IntegerField()
    id_seller = models.IntegerField()
    id_profile = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


class Admission(models.Model):
    id_cassette = models.IntegerField()
    id_seller = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.
