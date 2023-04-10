from django.db import models

# Create your models here.
#db테이블 만드는 것

class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self): #절대경로. 블로그 밑에 번호
        return f'/blog/{self.pk}'
