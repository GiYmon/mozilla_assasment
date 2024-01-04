from django.urls import reverse


def test_post_content(post):
    assert post.title == "A sample title"
    assert post.description == "A sample description"
    assert post.author.username == "testuser"


def test_post_str_representation(post):
    assert str(post) == post.title


def test_get_absolute_url(post):
    assert post.get_absolute_url() == reverse("post-detail", kwargs={"pk": post.pk})
