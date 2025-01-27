from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):  # New
    model = Comment


class ArticleAdmin(admin.ModelAdmin):   # New
    inlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)  # New
admin.site.register(Comment)