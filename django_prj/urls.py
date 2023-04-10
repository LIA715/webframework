"""django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #관리자 기능 사용 위한 패키지 가져옴
from django.urls import path,include #path 함수 사용

urlpatterns = [
    path("admin/", admin.site.urls), #주소 다음에 있는 주소로 연결하라는 뜻. router 역할
    path('', include('ssingle_pages.urls')), #아무것도 안들어왓어. 그러면 ssingle 의 urls로 가
    path('blog/', include('blog.urls')), #블로그를 위해서 관리자 서비스 계정에 등록되어있는 걸 가져와 -> 복잡

]
