from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts")
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self) -> str:
        return reverse("post-detail", kwargs={"pk": self.pk})


class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)

    def __str__(self) -> str:
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.body)
