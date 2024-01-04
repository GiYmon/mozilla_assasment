from typing import Any

from django.views.generic import DetailView, ListView, TemplateView

from .models import Author, Post


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
        context["posts"] = self.object.posts.all()
        return context
