from django.contrib.auth import get_user_model
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import resolve, reverse

from .models import Post
from .views import HomePageView

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


class BlogHomePageTest(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home.html")
        self.assertContains(self.response, "Home page")

    def test_homepage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepage(self):
        view = resolve("/blog/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        author = User.objects.create_user(username="testuser1", password="testpass1")

        for post_id in range(10):
            Post.objects.create(
                title=f"title {post_id}",
                description=f"desc {post_id}",
                author=author,
            )

    def setUp(self) -> None:
        url = reverse("list")
        self.response = self.client.get(url)

    def test_view_url_exists_at_correct_location(self):
        response = self.client.get("/blog/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessibile_by_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "blog/list.html")

    def test_pagination_is_five(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue("is_paginated" in self.response.context)
        self.assertTrue(self.response.context["is_paginated"] == True)
        self.assertEqual(len(self.response.context["blog_list"]), 5)

    def test_list_all_blogs(self):
        response = self.client.get(reverse("list") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in self.response.context)
        self.assertTrue(self.response.context["is_paginated"] == True)
        self.assertEqual(len(response.context["blog_list"]), 5)
