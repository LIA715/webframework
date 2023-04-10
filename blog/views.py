from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )

def single_post_page(request,pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post, #앞에가 변수명 뒤에가 객체
        }
    )
