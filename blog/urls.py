from django.urls import path

from .views import BlogListView, HomePageView

urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="list"),
    path("", HomePageView.as_view(), name="home"),
]
