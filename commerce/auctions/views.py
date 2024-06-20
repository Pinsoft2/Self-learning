from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User
from .models import Listing
from .models import Bid
from .models import Comment
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Max

class ListingView(generic.ListView):
    queryset = Listing.objects.order_by("-created_time")
    template_name = "auctions/index.html"

    def listings(self):
        return Listing.objects.all()


@login_required(login_url='/auctions/login')
def create_listing(request):
    if request.method == "POST":
        ins = Listing(
            title = request.POST["title"],
            starting_bid = request.POST["starting_bid"],
            description = request.POST["description"],
            category = request.POST["category"],
            image_url = request.POST["image_url"],
            user= request.user)
        ins.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "auctions/create_listing.html")


@login_required(login_url='/auctions/login')
def watchlist(request):
    currentUser = request.user
    listings = currentUser.ListingWatchlist.all()
    return render(request, "auctions/watchlist.html", {"listings" : listings})



class CategoryView(generic.ListView):
    queryset = Listing.objects.order_by("-created_time")
    template_name = "auctions/categories.html"

    def listings(self):
        return Listing.objects.distinct()


def listing(request, id):

    bid_count = len(Bid.objects.filter(item_id=id))
    max_bid = Bid.objects.filter(item_id=id).aggregate(Max('bid_price'))['bid_price__max']

    all_comment_content = Comment.objects.filter(item_id=id).values()

    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    return render(request, "auctions/listing.html", {
        "object" :listingData,
        "isListingInWatchlist" : isListingInWatchlist,
        "bid_count" : bid_count,
        "max_bid" : max_bid,
        "all_comment_content" : all_comment_content
    })

def comment(request,id):
    if request.method == "POST":
        newComment = Comment(
            comment_content = request.POST["comment_content"],
            item_id = id,
            user = request.user)
        newComment.save()
        return HttpResponseRedirect(reverse("listing",args=(id, )))
    else:
        return render(request, "auctions/create_listing.html")

def close(request,id):
    if request.method == "POST":
        entry = Listing.objects.filter(pk=id).update(status=0)
        return HttpResponseRedirect(reverse("listing",args=(id, )))
    else:
        return render(request, "auctions/create_listing.html")



def bid(request, id):
    if request.method == "POST":
        max_bid = Bid.objects.filter(item_id=id).aggregate(Max('bid_price'))['bid_price__max']

        starting_bid = Listing.objects.filter(pk=id).values()[0]['starting_bid']
        print(starting_bid)

        if max_bid is None:
            max_bid = starting_bid

        current_bid = float(request.POST["bid_price"].strip(' "'))

        if  current_bid > max_bid >= starting_bid > 0:
            newbid = Bid(
            bid_price = float(request.POST["bid_price"].strip(' "')) ,
            item_id = id,
            user = request.user)
            newbid.save()
            Bid_failure = False
        else:
            Bid_failure = True

        bid_count = len(Bid.objects.filter(item_id=id))
        max_bid = Bid.objects.filter(item_id=id).aggregate(Max('bid_price'))['bid_price__max']
        all_comment_content = Comment.objects.filter(item_id=id).values()
        listingData = Listing.objects.get(pk=id)
        isListingInWatchlist = request.user in listingData.watchlist.all()
        return render(request, "auctions/listing.html", {
            "object" :listingData,
            "isListingInWatchlist" : isListingInWatchlist,
            "bid_count" : bid_count,
            "max_bid" : max_bid,
            "all_comment_content" : all_comment_content,
            "Bid_failure" :Bid_failure
        })



def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    user= request.user
    listingData.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    user= request.user
    listingData.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

class RequireLoginMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around
    matching URL patterns. To use, add the class to MIDDLEWARE_CLASSES and
    define LOGIN_REQUIRED_URLS and LOGIN_REQUIRED_URLS_EXCEPTIONS in your
    settings.py. For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$',
        r'/topsecret/logout(.*)$',
    )
    ------
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must
    be a valid regex.

    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly
    define any exceptions (like login and logout URLs).
    """
    def __init__(self):
        self.required = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # No need to process URLs if user already logged in
        if request.user.is_authenticated():
            return None

        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path):
                return None

        # Requests matching a restricted URL pattern are returned
        # wrapped with the login_required decorator
        for url in self.required:
            if url.match(request.path):
                return login_required(view_func)(request, *view_args, **view_kwargs)

        # Explicitly return None for all non-matching requests
        return None

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
