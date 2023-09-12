from django.views.generic import ListView

from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# for restricting access using mixins
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# All for cancel button - ArticleCancelView
from django.views.generic import View # cancel button
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse


from .models import Article 

# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    # To block another user from editing another authors post
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

     # To block another user from deleting another authors post
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCancelView(LoginRequiredMixin, View):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        # Add your cancel logic here, if needed
        return redirect(reverse("article_detail", kwargs={"pk": pk}))
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
    )

    # function/method to make sure the author is same without the options of other authors in the database
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
