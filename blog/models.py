from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
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
