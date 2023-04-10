from django.urls import path,include #path 함수 사용
from .import views #현재 위치에서 views를 의미함.

urlpatterns = [
    path('', views.landing), #일종의 함수. views = 현 위치 > views.py를 의미함/ 계속 아무것도 없어. view-landing으로 가
    path('about_me/',views.about_me), #about_me랑 매칭. view > aboutme 함수를 불러라. (탬플릿 아래에 있는)

    #view = 클라이언트에게 화면을 보여주는 기능
    path('blog/', include('blog.urls')), #블로그를 위해서 관리자 서비스 계정에 등록되어있는 걸 가져와 -> 복잡

]
# /로 시작하면 절대 경로. /없으면 이전까지의 경로는 유지하되 추가적으로 가는 경로를 의미 = 상대 경로