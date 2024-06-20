# Generated by Django 5.0.3 on 2024-05-08 04:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0004_alter_post_liked_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="liked_by",
        ),
        migrations.AddField(
            model_name="post",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
