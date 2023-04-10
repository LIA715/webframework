from django.urls import path,include #path 함수 사용
from . import views
urlpatterns = [
    #path('',views.index), #서버주소 밑에 블로그 server/blog/ => 이게 주소가 됨
    path('',views.PostList.as_view()), #postlist에서 정해진 모델을 자동으로 가져오는 역할. 함수가 아니고 클래스라 동작을 못해.

    path('<int:pk>/',views.single_post_page), #server/blog/숫자 =>가 들어가는 상대적인 경로로 쓰여짐.
]
