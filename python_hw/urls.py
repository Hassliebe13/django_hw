from django.contrib import admin
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('/', main, name='main'),
    path('posts/', catalog_posts, name='catalog_posts'),
    path('categories/', catalog_categories, name='catalog_categories'),
    path('categories/<slug:category_slug>/', category_detail, name='category_detail'),
    path('tags/', catalog_tags, name='catalog_tags'),
    path('tags/<slug:tag_slug>/', tag_detail, name='tag_detail'),
]