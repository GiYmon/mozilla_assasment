import pytest
from django.utils.dateparse import parse_datetime

from ..api.serializers import AuthorSerializer, CommentSerializer, PostSerializer
from ..factories import AuthorFactory, CommentFactory, PostFactory


@pytest.mark.django_db
def test_author_serializer():
    author = AuthorFactory()
    serializer = AuthorSerializer(author)

    assert serializer.data == {
        "id": author.id,
        "user": author.user.id,
        "bio": author.bio,
    }

    # Test deserialization and validation
    data = {"user": author.user.id, "bio": "New bio"}
    serializer = AuthorSerializer(data=data)
    assert serializer.is_valid()
    new_author = serializer.save()
    assert new_author.bio == "New bio"


@pytest.mark.django_db
def test_post_serializer():
    post = PostFactory()
    serializer = PostSerializer(post)
    # Parse both datetimes
    expected_post_date = parse_datetime(post.post_date.isoformat())
    serialized_post_date = parse_datetime(serializer.data["post_date"])

    # Test serialization
    assert serializer.data["id"] == post.id
    assert serializer.data["title"] == post.title
    assert serializer.data["description"] == post.description
    assert serializer.data["author"] == post.author.id
    assert serialized_post_date == expected_post_date
    # Test deserialization and validation
    data = {"title": "New Post", "description": "Description", "author": post.author.id}
    serializer = PostSerializer(data=data)
    assert serializer.is_valid()
    new_post = serializer.save()
    assert new_post.title == "New Post"


@pytest.mark.django_db
def test_comment_serializer():
    comment = CommentFactory()
    serializer = CommentSerializer(comment)
    # Test serialization
    assert serializer.data == {
        "id": comment.id,
        "author": comment.author.id,
        "post": comment.post.id,
        "body": comment.body,
    }
    # Test deserialization and validation
    data = {"author": comment.author.id, "post": comment.post.id, "body": "New comment"}
    serializer = CommentSerializer(data=data)
    assert serializer.is_valid()
    new_comment = serializer.save()
    assert new_comment.body == "New comment"
