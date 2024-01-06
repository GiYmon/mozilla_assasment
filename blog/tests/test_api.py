import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import PostFactory


@pytest.mark.django_db
def test_post_list(client):
    PostFactory.create_batch(5)
    url = reverse("post-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@pytest.mark.django_db
def test_post_retrieve(client):
    post = PostFactory()
    url = reverse("post-detail", args=[post.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == post.id
