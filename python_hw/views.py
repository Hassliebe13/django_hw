from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Категории
CATEGORIES = [
        {'slug': 'python', 'name': 'Python'},
        {'slug': 'django', 'name': 'Django'},
        {'slug': 'postgresql', 'name': 'PostgreSQL'},
        {'slug': 'docker', 'name': 'Docker'},
        {'slug': 'linux', 'name': 'Linux'},
    ]

# Теги
TAGS = [
    {'slug': 'framework', 'name': 'Framework'},
    {'slug': 'database', 'name': 'Database'},
    {'slug': 'backend', 'name': 'Backend'},
    {'slug': 'frontend', 'name': 'Frontend'},
    {'slug': 'devops', 'name': 'DevOps'},
    {'slug': 'testing', 'name': 'Testing'},
    {'slug': 'api', 'name': 'API'},
    {'slug': 'security', 'name': 'Security'}
]

# URL константы
CATEGORIES_URL = reverse_lazy('blog:catalog_categories')
TAGS_URL = reverse_lazy('blog:catalog_tags')
POSTS_URL = reverse_lazy('blog:catalog_posts')
MAIN_URL = reverse_lazy('blog:main')

# Главная страница
def main(request):
    return HttpResponse(f"""
            <h1>Главная страница</h1>
                <p><a href="{POSTS_URL}">Каталог постов</a></p>
        """)

# Каталог категорий
def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url = reverse('blog:category_detail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')
    return HttpResponse(f"""
                        <h1>Каталог категорий</h1>
                        {''.join(links)}
                        """)

# Каталог тегов
def catalog_tags(request):
    links = []
    for tags in TAGS:
        url = reverse('blog:tag_detail', args=[tags['slug']])
        links.append(f'<p><a href="{url}">{tags["name"]}</a></p>')
    return HttpResponse(f"""
                        <h1>Каталог категорий</h1>
                        {''.join(links)}
                        """)

# Каталог постов
def catalog_posts(request):
    return HttpResponse(f"""<h1>Каталог постов</h1>
                        <p><a href="{CATEGORIES_URL}">Каталог категорий</a></p>
                        <p><a href="{TAGS_URL}">Каталог тегов</a></p>
                        """)

# Детальная страница категории
def category_detail(request, category_slug):
    category_name = category_slug.replace('-', ' ').title()
    categories_url = reverse('blog:catalog_categories')
    
    return HttpResponse(f"""
                        <h1>Категория: {category_name}</h1>
                        <div class="category-content">
                            <p>Здесь будет отображаться содержимое категории {category_name}</p>
                        </div>
                        <p><a href="{categories_url}">Вернуться к списку категорий</a></p>
                        """)

# Детальная страница тега
def tag_detail(request, tag_slug):
    tag_name = tag_slug.replace('-', ' ').title()
    tags_url = reverse('blog:catalog_tags')
    return HttpResponse(f""" 
                        <h1>Тег: {tag_name}</h1>
                        <div class="tag-content">
                            <p>Здесь будет отображаться содержимое тега {tag_name}</p>
                        </div>
                        <p><a href="{tags_url}">Вернуться к списку тегов</a></p>
                        """)