from django.db import models


# Create your models here.
class Collection(models.Model):
    chain = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)
    supply = models.IntegerField()
    symbol = models.CharField(max_length=32)
    discord_link = models.CharField(max_length=512)
    twitter_link = models.CharField(max_length=512)
    website_link = models.CharField(max_length=512)
    imageURI = models.CharField(max_length=1024)


class CollectionStat(models.Model):
    collection = models.OneToOneField(Collection, on_delete=models.CASCADE)
    floor_price = models.CharField(max_length=128)
    inscription_number_min = models.CharField(max_length=128)
    inscription_number_max = models.CharField(max_length=128)
    owners = models.CharField(max_length=32)
    pending_transactions = models.IntegerField()
    supply = models.IntegerField()
    total_listed = models.IntegerField()
    total_volume = models.IntegerField()


class CollectionToken(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    collection_symbol = models.CharField(max_length=32)
