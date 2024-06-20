from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


#Because it inherits from AbstractUser, it will already have fields for a username, email, password, etc.
class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=1000)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    image_url = models.URLField(max_length=500, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    watchlist = models.ManyToManyField(User,blank=True,default=False,related_name="ListingWatchlist")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Bid(models.Model):
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    submitted_time =  models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item_id = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item_id = models.IntegerField()
    comment_content = models.TextField(blank=True)




# Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).

#Models: Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.

