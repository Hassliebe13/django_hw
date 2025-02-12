from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .constant import MENU_ITEMS, CATEGORIES, TAGS, POSTS

# URL константы
CATEGORIES_URL = reverse_lazy('blog:catalog_categories')
TAGS_URL = reverse_lazy('blog:catalog_tags')
POSTS_URL = reverse_lazy('blog:catalog_posts')
MAIN_URL = reverse_lazy('blog:main')

# Главная страница
def main(request):
    context = {
        'title': 'Главная страница',
        'menu_items': MENU_ITEMS,
        'posts': [post for post in POSTS if post['is_published']][:2]
    }
    return render(request, 'main.html', context)

def about(request):
    context = {
        'title': 'О проекте',
        'menu_items': MENU_ITEMS,
        'user_count': 100,
        'posts': POSTS
    }
    return render(request, 'about.html', context)

# Каталог категорий
def catalog_categories(request):
    context = {
        'title': 'Каталог категорий',
        'categories': CATEGORIES,
        'menu_items': MENU_ITEMS
    }
    return render(request, 'catalog.html', context)

# Каталог тегов
def catalog_tags(request):
    context = {
        'title': 'Каталог тегов',
        'tags': TAGS,
        'menu_items': MENU_ITEMS
    }
    return render(request, 'teg.html', context)

# Каталог постов
def catalog_posts(request):
    context = {
        'title': 'Каталог постов',
        'posts': POSTS,
        'menu_items': MENU_ITEMS
    }
    return render(request, 'posts_list.html', context)

def post_detail(request, post_slug):
    post = next((post for post in POSTS if post['slug'] == post_slug), None)
    context = {
        'title': post['title'],
        'post': post,
        'menu_items': MENU_ITEMS
    }
    return render(request, 'post_detail.html', context)


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