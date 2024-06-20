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
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"{self.user}: {self.new_post_content[:10]}..."

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "new_post_content": self.new_post_content,
            "image_url": self.image_url,
            "created_time": self.created_time.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.liked_by.count(),
        }

# posts, likes, and followers
# python manage.py makemigrations and then python manage.py migrate
