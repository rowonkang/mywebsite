from django.urls import path
from blog import views


# 2020.02.04 Conclusion. views.py index() 함수 return 값에서, 'blog/index.html'과 대응.
# 1. app_name = 'blog' + views.py.index().return render('request', 'blog/index.html', ...) : templates/blog/index.html 실행.
# 2. (# app_name = 'blog') 없이, views.py.index().return render('request', 'index.html', ...) :  templates/index.html 실행.
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
]

# print("post.get_absolute_url : ", post.get_absolute_url)

# path('single/', views.single, name='single'), => path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),