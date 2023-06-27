from django.urls import path

from .views import ReviewView, ReviewListView

urlpatterns = [
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    path("review/<slug:slug>/", ReviewView.as_view(), name="blog-detail"),

]
