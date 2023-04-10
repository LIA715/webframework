from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post #db 접근이 model 접근임. from으로 불러와

# Create your views here.
def index(request):
    posts=Post.objects.all() #모두 가져와 all posts=변수.

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts, #추가적으로 보내고싶은건 더 쓰면됨.
        }
    )

def single_post_page(request,pk):
    post = Post.objects.get(pk=pk) #특정 위치의 것을 가져와 get post라는 이름으로 하나만 넘기겠다.
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post, #앞에가 변수명 뒤에가 객체
        }
    )
