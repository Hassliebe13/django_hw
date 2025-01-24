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
            <p><a href="{POSTS_URL}">Каталог постов</a></p>
        """)

def catalog_categories(reqest):
    links = []
    for category in CATEGORIES:
        url = reverse('blog:category_detail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')
    return HttpResponse(f"""
                        <h1>Каталог категорий</h1>
                        {''.join(links)}
                        <p><a href="{reverse('blog:catalog_posts')}">К списку постов</a></p>
                        """)

def category_detail(request):
    return HttpResponse(f"""
        <h1>Категория</h1>
            <p><a></a></p>
            <p><a></a></p>
                        """)

def catalog_tags(request):
    return HttpResponse(f"""
        <h1>Каталог тегов</h1>
            <p><a></a></p>
            <p><a></a></p>
                        """)

def tag_detail(request):
    return HttpResponse(f"""
        <h1>Тег</h1>
            <p><a></a></p>
            <p><a></a></p>
                        """)

def catalog_posts(request):
    return HttpResponse(f"""
        <h1>Каталог постов</h1>
        <p><a href="{CATEGORIES_URL}">Каталог категорий</a></p>
        <p><a href="{TAGS_URL}">Каталог тегов</a></p>
                        """)