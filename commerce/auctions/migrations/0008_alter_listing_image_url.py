# Generated by Django 4.2.6 on 2024-01-15 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0007_listing_watchlist_delete_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image_url",
            field=models.URLField(max_length=500, null=True),
        ),
    ]
