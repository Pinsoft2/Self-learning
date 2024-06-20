from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListingView.as_view(), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path('listing/<int:id>/', views.listing, name = 'listing'),
    path("categories", views.CategoryView.as_view(), name="categories"),
    path("addWatchlist/<int:id>/", views.addWatchlist, name="addWatchlist"),
    path("removeWatchlist/<int:id>/", views.removeWatchlist, name="removeWatchlist"),
    path("bid/<int:id>/", views.bid, name="bid"),
    path("close/<int:id>/", views.close, name="close"),
    path("comment/<int:id>/", views.comment, name="comment"),
]
