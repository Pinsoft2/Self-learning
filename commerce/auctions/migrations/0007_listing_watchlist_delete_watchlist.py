# Generated by Django 4.2.6 on 2024-01-15 04:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_watchlist_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True,
                default=False,
                related_name="ListingWatchlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Watchlist",
        ),
    ]
