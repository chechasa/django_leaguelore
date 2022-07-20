from django.db import models

# Create your models here.
class Players(models.Model):
    summoner_name = models.CharField(max_length=50)
    summoner_level = models.IntegerField()
    profileIconId = models.IntegerField()
    slug = models.SlugField(unique=True)
    encryptedSummonerId = models.CharField(max_length=150)