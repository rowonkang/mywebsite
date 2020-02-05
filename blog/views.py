from django.shortcuts import render
from blog.models import Category, Post
from django.views import generic

from django.conf import settings

# def index(request):
#     context = {
#     }
#     return render(request, 'index.html', context=context)
#     # return render(req, 'blog/index.html', context=context)  # 아래 결론 참조
#     # return render(request, 'templates/index.html', context=context) : 이렇게 'templates'를 넣고 실행하면, 에러 발생.
#     # 2020.02.04 Conclusion. views.py index() 함수 return 값에서, 'blog/index.html'과 대응.
#     # 1. app_name = 'blog' + views.py.index().return render('request', 'blog/index.html', ...) : templates/blog/index.html 실행.
#     # 2. (# app_name = 'blog') 없이, views.py.index().return render('request', 'index.html', ...) :  templates/index.html 실행.

def index(request):
    post_latest = Post.objects.order_by('-createDate')[:6]
    context = {
        'post_latest': post_latest,
        'base_dir': settings.BASE_DIR,
        'static_url': settings.STATIC_URL,
        'static_root': settings.STATIC_ROOT,
    }
    return render(request, 'blog/index.html', context)
    # 'static_root': settings.STATIC_ROOT,
    # 'staticfiles_dir': settings.STATICFILES_DIR,
    # return render(req, 'blog/index.html', context=context)  # 아래 결론 참조
    # return render(request, 'templates/index.html', context=context) : 이렇게 'templates'를 넣고 실행하면, 에러 발생.
    # 2020.02.04 Conclusion. views.py index() 함수 return 값에서, 'blog/index.html'과 대응.
    # 1. app_name = 'blog' + views.py.index().return render('request', 'blog/index.html', ...) : templates/blog/index.html 실행.
    # 2. (# app_name = 'blog') 없이, views.py.index().return render('request', 'index.html', ...) :  templates/index.html 실행.

class PostDetailView(generic.DetailView):
    model = Post



# def single(request):
#     context = {
#     }
#     return render(request, 'blog/single.html', context)
