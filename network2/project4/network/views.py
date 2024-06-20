from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import Post
from django.db.models import Count
#backend pagination
from django.core.paginator import Paginator
from django.http import JsonResponse

def index(request):
    posts = Post.objects.annotate(likes=Count('liked_by'))
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html",
                  {"posts" : posts, 'page_obj':page_obj}
                )



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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")




def create_post(request):
    if request.method == "POST":
        ins = Post(
            new_post_content = request.POST["new_post_content"],
            image_url = request.POST["image_url"],
            user= request.user)
        ins.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "auctions/create_post.html")


def following(request):
    posts = Post.objects.filter(
        user__in=request.user.following.all() | User.objects.filter(pk=request.user.pk)
    ).annotate(likes=Count('liked_by'))

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/following.html",
                  {"posts" : posts,
                   'page_obj':page_obj}
                )


def profile(request, user_id):
    # Get the user whose profile is being viewed
    profile_user = User.objects.get(id=user_id)

    # Get the posts of the user
    posts = Post.objects.filter(user=profile_user).annotate(likes=Count('liked_by'))

    # Get the follower count
    follower_count = profile_user.followers.count()

    # Get the following count
    following_count = profile_user.following.count()

    # Get following_status from session (default to False if not found)
    following_status = request.session.get('following_status', False)


    return render(request, "network/profile.html", {
        "posts": posts,
        "profile_user": profile_user,
        "follower_count": follower_count,
        "following_count": following_count,
         "following_status": following_status
    })


def follow(request, user_id):
    current_user = request.user
    #get original poster's data
    #add to the followers
    user_to_follow = User.objects.get(id=user_id)
    user_to_follow.followers.add(current_user)
    following_status = True
    #add to followings
    current_user.following.add(user_to_follow)
    print("followed!")

    # Add following_status to session
    request.session['following_status'] = following_status

    return HttpResponseRedirect(reverse("profile",args=(user_id, )))


def unfollow(request, user_id):
    current_user = request.user
    #get original poster's data
    user_to_follow = User.objects.get(id=user_id)
    user_to_follow.followers.remove(current_user)
    following_status = False
    # remove from following
    current_user.following.remove(user_to_follow)
    print("unfollowed!")

    # Add following_status to session
    request.session['following_status'] = following_status

    return HttpResponseRedirect(reverse("profile",args=(user_id, )))

#python code is what determines what's stored in the database (Server side)
def like_post(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        user = request.user
        like_status = False

        if user not in post.liked_by.all():
            post.liked_by.add(user)
            like_status = True
        else:
            post.liked_by.remove(user)
            like_status = False
        post.save()

        return JsonResponse({'like_status': like_status, 'likes_count': post.liked_by.count()})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


