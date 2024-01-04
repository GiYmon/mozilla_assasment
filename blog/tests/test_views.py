import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_page_view(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "home.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_blog_list_view(client, posts):
    url = reverse("post-list")
    response = client.get(url)
    assert response.status_code == 200
    assert "blog/list.html" in [t.name for t in response.templates]
    assert len(response.context["blog_list"]) == 5  # Check pagination
    assert response.context["blog_list"][0].title == "Sample title 9"  # Check ordering


@pytest.mark.django_db
def test_blog_detail_view(client, posts):
    post = posts[0]
    url = reverse("post-detail", kwargs={"pk": post.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert "blog/detail.html" in [t.name for t in response.templates]
    assert response.context["post"] == post
