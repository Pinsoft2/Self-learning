# Generated by Django 4.2.6 on 2024-01-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0009_bid_bid_price_bid_item_id_bid_submitted_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]
