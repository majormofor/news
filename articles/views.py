from typing import Any
from django.http import HttpResponse
from django.views.generic import ListView

from django.views.generic import DetailView
# for comment
from django.views import View
# to add comment fields
from .forms import CommentForm
# To post comment
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

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

    # to show comment fields
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


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



class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs ):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})

class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    