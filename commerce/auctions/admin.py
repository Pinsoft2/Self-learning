from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("title", "starting_bid", "created_time", "category","starting_bid")
    list_filer = ("category")
    search_fields = ("title","category")


admin.site.register(Listing, ListingsAdmin)