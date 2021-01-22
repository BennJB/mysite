from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# 최상위 urlconf에서 polls/를 전달받으면, views.index 내부로 연결을 시킨다.