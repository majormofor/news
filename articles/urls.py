from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCancelView,
    ArticleCreateView

)

urlpatterns = [
    path("<int:pk>", ArticleDetailView.as_view(), name= "article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name= "article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name= "article_delete"),
    path('article/<int:pk>/cancel/', ArticleCancelView.as_view(), name='cancel_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),

    path("", ArticleListView.as_view(), name= "article_list"),
]