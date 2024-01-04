from django.urls import path

from .views import AuthorListView, BlogDetailView, BlogListView, HomePageView

urlpatterns = [
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("blogs/", BlogListView.as_view(), name="post-list"),
    path("bloggers/", AuthorListView.as_view(), name="authors-list"),
    path("", HomePageView.as_view(), name="home"),
]
