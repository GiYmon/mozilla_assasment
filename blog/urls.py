from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/create/", views.CommentCreateView.as_view(), name="create-comment"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="post-detail"),
    path("blogs/", views.BlogListView.as_view(), name="post-list"),
    path("blogger/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("bloggers/", views.AuthorListView.as_view(), name="author-list"),
    path("", views.HomePageView.as_view(), name="home"),
]
