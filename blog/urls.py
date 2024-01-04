from django.urls import path

from .views import BlogDetailView, BlogListView, HomePageView

urlpatterns = [
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("blogs/", BlogListView.as_view(), name="post-list"),
    path("", HomePageView.as_view(), name="home"),
]
