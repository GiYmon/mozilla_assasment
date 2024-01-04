import pytest
from django.contrib.auth import get_user_model

from ..models import Author, Post


@pytest.fixture
def user(db):
    """
    Creates a user.
    """
    return get_user_model().objects.create_user(username="testuser", password="12345")


@pytest.fixture
def author(user) -> Author:
    """
    Creates a author.
    """
    return Author.objects.create(user=user, bio="Sample bio")


@pytest.fixture
def posts(author) -> list[Post]:
    """
    Creates a list of 10 posts.
    """
    return [
        Post.objects.create(
            title=f"Sample title {i}",
            description="Sample description",
            author=author,
        )
        for i in range(10)
    ]


@pytest.fixture
def post(author) -> Post:
    """
    Creates a post
    """
    return Post.objects.create(
        title="A sample title",
        description="A sample description",
        author=author,
    )
