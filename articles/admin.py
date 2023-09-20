from django.contrib import admin
from .models import Article, Comment

# Register your models here.

# To view each comment in stacked form (fields in different line)
# class CommentInline(admin.StackedInline):
# To view each comment in tabular form(field in same line)
class CommentInline(admin.TabularInline):
    model = Comment
    # to remove extra comment empty field
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
   inlines = [
       CommentInline,
   ]
   list_display = [
    "title",
    "body",
    "author",
   ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)