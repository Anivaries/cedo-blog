from django.urls import path

from .views import BlogView

urlpatterns = [
    path("<slug:slug>/", BlogView.as_view(), name="blog-detail")
]
