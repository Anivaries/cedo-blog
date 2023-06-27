from django.urls import path

from .views import ReviewView, ReviewListView, ArticlesListView

urlpatterns = [
    path("", ArticlesListView.as_view(), name="articles"),
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    path("review/<slug:slug>/", ReviewView.as_view(), name="blog-detail"),


]
