from django.urls import path
from .views import BookmarksList, BookmarksDetail

urlpatterns = [
    path('', BookmarksList.as_view(), name='bookmarks_list'),
    path('<int:pk>/', BookmarksDetail.as_view(), name='bookmarks_detail'),
]
