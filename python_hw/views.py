from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

CATEGORIES = [
        {'slug': 'python', 'name': 'Python'},
        {'slug': 'django', 'name': 'Django'},
        {'slug': 'postgresql', 'name': 'PostgreSQL'},
        {'slug': 'docker', 'name': 'Docker'},
        {'slug': 'linux', 'name': 'Linux'},
    ]

# URL константы
CATEGORIES_URL = reverse_lazy('blog:catalog_categories')
TAGS_URL = reverse_lazy('blog:catalog_tags')
POSTS_URL = reverse_lazy('blog:catalog_posts')
MAIN_URL = reverse_lazy('blog:main')

def main(request):
    return HttpResponse(f"""
            <h1>Главная страница</h1>
            <p><a href="{CATEGORIES_URL}">Каталог категорий</a></p>
            <p><a href="{TAGS_URL}">Каталог тегов</a></p>
        """)

def catalog_categories(request):
    return HttpResponse("<h1>Каталог категорий</h1>")

def catalog_posts(request):
    return HttpResponse("<h1>Каталог постов</h1>")

def category_detail(request, category_slug):
    return HttpResponse(f"<h1>Категория: {category_slug}</h1>")

def catalog_tags(request):
    return HttpResponse("<h1>Каталог тегов</h1>")

def tag_detail(request, tag_slug):
    return HttpResponse(f"<h1>Тег: {tag_slug}</h1>")