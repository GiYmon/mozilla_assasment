from django.urls import path

from .views import (
    AuthorDetailView,
    AuthorListView,
    BlogDetailView,
    BlogListView,
    HomePageView,
)

urlpatterns = [
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("blogs/", BlogListView.as_view(), name="post-list"),
    path("blogger/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("bloggers/", AuthorListView.as_view(), name="author-list"),
    path("", HomePageView.as_view(), name="home"),
]
