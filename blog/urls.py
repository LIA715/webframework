from django.urls import path,include #path 함수 사용
from . import views
urlpatterns = [
    path('',views.index), #서버주소 밑에 블로그 server/blog/ => 이게 주소가 됨
    path('<int:pk>/',views.single_post_page), #server/blog/숫자 =>가 들어가는 상대적인 경로로 쓰여짐.
]
