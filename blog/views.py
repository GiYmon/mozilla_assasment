from django.views.generic import ListView, TemplateView

from .models import Post


class HomePageView(TemplateView):
    template_name = "home.html"


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = "blog_list"
    paginate_by = 5
    ordering = ["-post_date"]
