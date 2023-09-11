from django.views.generic import ListView

from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# for creating an article


# All for cancel button - ArticleCancelView
from django.views.generic import View # cancel button
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse


from .models import Article 

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

class ArticleCancelView(View):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        # Add your cancel logic here, if needed
        return redirect(reverse("article_detail", kwargs={"pk": pk}))
    
class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
