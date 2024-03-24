from django.urls import path
from .views import CommentsList, CommentsDetail

urlpatterns = [
    path('', CommentsList.as_view(), name='comments_list'),
    path('<int:pk>/', CommentsDetail.as_view(), name='comments_detail'),
]
