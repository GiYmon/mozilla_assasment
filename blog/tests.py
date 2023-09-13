from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="testuser1", password="testpass1")

    def test_saving_post(self):
        post = Post.objects.create(
            title="test1", description="This is the first post", author=self.user
        )

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, "test1")

    def test_string_representation(self):
        post = Post.objects.create(
            title="test1", description="This is the first post", author=self.user
        )

        self.assertEqual(str(post), post.title)

    def test_saving_and_retrieving_posts(self):
        first_post = Post.objects.create(
            title="test1", description="This is the first post", author=self.user
        )
        second_post = Post.objects.create(
            title="test2", description="This is the second post", author=self.user
        )

        saved_items = Post.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.title, "test1")
        self.assertEqual(first_saved_item.description, "This is the first post")
        self.assertEqual(first_saved_item.author, self.user)
        self.assertEqual(second_saved_item.title, "test2")
        self.assertEqual(second_saved_item.description, "This is the second post")
        self.assertEqual(second_saved_item.author, self.user)
