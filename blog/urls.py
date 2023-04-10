from django.urls import path,include #path 함수 사용
from . import views
urlpatterns = [
    path('',views.index),
    path('<int:pk/>',views.single_post_page),
]
