from django.contrib import admin

from .models import Author, Comment, Post

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
