# from django.views import generic
from django.views.generic import DetailView
from .models import Blog

class BlogView(DetailView):
    model = Blog
    template_name = "blog_content.html"

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        context["blog"] = Blog.objects.filter(slug=slug)
        return context
    