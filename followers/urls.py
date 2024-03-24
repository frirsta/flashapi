from django.urls import path
from .views import FollowersList, FollowersDetail

urlpatterns = [
    path('', FollowersList.as_view(), name='followers_list'),
    path('<int:pk>/', FollowersDetail.as_view(), name='followers_detail'),
]
