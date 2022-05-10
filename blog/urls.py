from . import views
from django.urls import path

urlpatterns =[
    #path('',views.index),
    path('<int:pk>/',views.single_post_page), #정수 형태의 값을 pk에 담아 single_post_page의 함수로 처리
    path('',views.PostList.as_view()),
]