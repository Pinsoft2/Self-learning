from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField("User", related_name="User_follower")
    following = models.ManyToManyField("User", related_name="User_following")
    pass

class Post(models.Model):
    new_post_content = models.CharField(max_length=1000)
    image_url = models.URLField(max_length=500, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    # liked_by = models.ForeignKey("User", on_delete=models.CASCADE,related_name="Post_liked_by", blank=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

