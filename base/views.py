# from django.views import generic
from typing import Any, Dict
from django.views.generic import DetailView, ListView
from .models import Article

class ArticlesListView(ListView):
    model = Article
    template_name = "articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all().order_by('-pub_date')
        return context
    
class ReviewView(DetailView):
    model = Article
    template_name = "blog_content.html"

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        context["blog"] = Article.objects.filter(slug=slug).filter(category="Review")
        return context
    
class ReviewListView(ListView):
    model = Article
    template_name = "review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Article.objects.filter(category="Review").order_by('-pub_date')
        return context
    
class OpinionListView(ListView):
    model = Article
    template_name = "opinion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opinion'] = Article.objects.filter(category="Opinion").order_by('-pub_date')
        return context
    
class HardwareListView(ListView):
    model = Article
    template_name = "hardware.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hardware'] = Article.objects.filter(category="Hardware").order_by('-pub_date')
        return context
    
class NewsListView(ListView):
    model = Article
    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Article.objects.filter(category="News").order_by('-pub_date')
        return context