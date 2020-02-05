from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='블로그 글의 카테고리를 입력하시오. (ex:일상)')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    # ImageField() 사용을 위해서는 settings.py 파일에 MEDIA_URL 변수를 세팅해 주어야 한다.
    title_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    # 하나의 글이 여러가자의 카테고리에 해당될 수 있고, (ex:정보, 유머),
    # 하나의 카테고리에는 여러개의 글이 있을 수 있다. (정보 카테고리에 10개의 글)
    category = models.ManyToManyField(Category, help_text='글의 카테고리를 선택하시오!')

    def __str__(self):
        return self.title

    # 브라우저 주소 창에 1번 글을 보내야 할 경우 : blog/single/1
    def get_absolute_url(self):
        print("str(self.id) : ", str(self.id))
        print("'/blog/post/{}/'.format(self.pk) :", '/blog/post/{}/'.format(self.pk))
        print("reverse('blog:post', kwargs={'pk': str(self.id)}) : ", reverse('blog:post', kwargs={'pk': str(self.id)}))
        print("reverse('blog:post', args=[str(self.id)]) : ", reverse('blog:post', args=[str(self.id)]))
        return '/blog/post/{}/'.format(self.pk)
        # return reverse('blog:post', kwargs={'pk': str(self.id)})
        # return reverse('blog:post', args=[str(self.id)])

        # 1 return '/blog/post/{}/'.format(self.pk)
        # 2 return reverse('blog:post', kwargs={'pk': str(self.id)})
        # 3 return reverse('blog:post', args=[str(self.id)])
        # 3 return reverse('blog:single', args=[str(self.id)])

        # 2020.02.06 Conclusion. ***** 엄청 해맨 후 얻은 결론 *****
        # 1. 일단 모든 폴더 관리는 원칙대로 하는 것이 에러를 최소화하는 것이다.
        # 2. mywebsite/blog/static/blog/ : 항상 이런 형태가 원칙이나, 여기 mywebsite 프로젝트에서는 그러하지 못한 관계로 엄청난 에러를 유발하였다.
        # 3. mywebsite/blog/templates/blog/ : 항상 이런 형태가 원칙이다.
        # 4. 또한 get_absolute_url() 함수의 return 값으로는, 위의 1,2,3 모두 사용 가능하다, 단, 아주 중요한 사실은,
        #    1항 2항과 3항 모두 반드시, 'blog:post'로 처리해야 한다.
        #    강의 내용과 같이 'post'로 처리하면, 평생 404 또는 500 에러를 화면에서 보게 될 것이다.

    # 글 내용.content가 300 글자 이상인지 확인. 300 글자 이상이면, True
    def is_content_more300(self):
        return len(self.content) > 300

    # 글 내용.content에서 300 글자만 리턴.
    def get_content_under300(self):
        return self.content[:300]


