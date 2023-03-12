from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_list, name='group_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('auto/', views.auto, name='auto'),
    path('moto/', views.moto, name='moto'),
    path('ja_auction/', views.ja_auction, name='ja_auction'),
    path('georgia/', views.georgia, name='georgia'),
]
