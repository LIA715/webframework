from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts=Post.objectss.all()

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )

def single_post_page(request,pk):
    return render(
        request,
        'blog/single_post_page.html',
    )
