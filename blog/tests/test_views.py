import pytest
from django.urls import reverse

from ..factories import AuthorFactory, PostFactory


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


@pytest.mark.django_db
def test_bloggers_list_view(client):
    bloggers = [AuthorFactory() for _ in range(5)]
    url = reverse("author-list")
    response = client.get(url)
    assert response.status_code == 200
    assert "author/list.html" in [t.name for t in response.templates]
    assert len(response.context["authors"]) == 5
    for blogger in bloggers:
        assert blogger.user.username in response.content.decode()


@pytest.mark.django_db
def test_blogger_detail_view(client):
    author = AuthorFactory()
    posts = [PostFactory(author=author) for _ in range(5)]
    url = reverse("author-detail", kwargs={"pk": author.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert "author/detail.html" in [t.name for t in response.templates]
    assert response.context["author"] == author
    assert list(response.context["posts"]) == posts
    for post in posts:
        assert post.title in response.content.decode()
