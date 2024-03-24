from django.urls import path
from .views import LikesList, LikesDetail


urlpatterns = [
    path('', LikesList.as_view(), name='likes_list'),
    path('<int:pk>/', LikesDetail.as_view(), name='likes_detail'),
]
