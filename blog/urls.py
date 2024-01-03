from django.urls import path

from .views import BlogDetailView, BlogListView, HomePageView

urlpatterns = [
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("blogs/", BlogListView.as_view(), name="list"),
    path("", HomePageView.as_view(), name="home"),
]
