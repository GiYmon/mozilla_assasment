import pytest
from django.urls import reverse

from ..factories import CommentFactory


def test_post_content(post):
    assert post.title == "A sample title"
    assert post.description == "A sample description"
    assert post.author.user.username == "testuser"


def test_post_str_representation(post):
    assert str(post) == post.title


def test_get_absolute_url(post):
    assert post.get_absolute_url() == reverse("post-detail", kwargs={"pk": post.pk})


def test_author_creation(author):
    assert author.user.username == "testuser"
    assert author.bio == "Sample bio"


def test_author_str_representation(author):
    assert str(author) == "testuser"


@pytest.mark.django_db
def test_comment_creation():
    comment = CommentFactory()

    assert comment.author is not None
    assert comment.post is not None
    assert len(comment.body) <= 255


@pytest.mark.django_db
def test_comment_str_representation():
    comment_body = "This is a test comment."
    comment = CommentFactory(body=comment_body)

    assert str(comment) == comment_body
