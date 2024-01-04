import pytest
from django.contrib.auth import get_user_model

from ..models import Post


@pytest.fixture
def user(db):
    """
    Creates a user.
    """
    return get_user_model().objects.create_user(username="testuser", password="12345")


@pytest.fixture
def posts(user) -> list[Post]:
    """
    Creates a list of 10 posts.
    """
    return [
        Post.objects.create(
            title=f"Sample title {i}",
            description="Sample description",
            author=user,
        )
        for i in range(10)
    ]


@pytest.fixture
def post(user) -> Post:
    """
    Creates a post
    """
    return Post.objects.create(
        title="A sample title",
        description="A sample description",
        author=user,
    )
