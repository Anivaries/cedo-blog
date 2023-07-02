from django.urls import path

from .views import ReviewView, ReviewListView, ArticlesListView, OpinionListView, HardwareListView, NewsListView, contact

urlpatterns = [
    path("", ArticlesListView.as_view(), name="articles"),
    path("contact/", contact, name="contact"),
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    path("opinions/", OpinionListView.as_view(), name="opinion"),
    path("hardware/", HardwareListView.as_view(), name="hardware"),
    path("news/", NewsListView.as_view(), name="news"),
    path("<slug:slug>/", ReviewView.as_view(), name="blog-detail"),
    
]
