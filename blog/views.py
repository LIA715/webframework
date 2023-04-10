from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post #db 접근이 model 접근임. from으로 불러와

# Create your views here.

class PostList(ListView): #List에서는 모델명_list.html을 찾도록 자동 설정 되어있음. >>post_list.html이 자동 생성
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html' #템플릿이 바뀜. 자동으로 바뀜


# def index(request):
#     posts=Post.objects.all() #모두 가져와 all posts=변수.
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts, #추가적으로 보내고싶은건 더 쓰면됨.
#         }
#     )
#
def single_post_page(request,pk):
    post = Post.objects.get(pk=pk) #특정 위치의 것을 가져와 get post라는 이름으로 하나만 넘기겠다.
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post, #앞에가 변수명 뒤에가 객체
        }
    )
