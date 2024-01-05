from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import CommentForm
from .models import Author, Comment, Post


class HomePageView(TemplateView):
    template_name = "home.html"


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = "blog_list"
    paginate_by = 5
    ordering = ["-post_date"]


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    queryset = Post.objects.all()


class AuthorListView(ListView):
    model = Author
    template_name = "author/list.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author/detail.html"
    queryset = Author.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.posts.order_by("-post_date")
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("post-detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["pk"])
        return context
