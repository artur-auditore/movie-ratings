from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Starring(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        ordering = ('name',)

class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    starring = models.ForeignKey(Starring, on_delete=models.CASCADE, related_name='starrings')

class Rate(models.Model):
    note = models.IntegerField()
    title = models.ForeignKey(Title, related_name='titles', on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ratings = models.ManyToManyField(Rate, related_name='ratings')