from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django.db.models import Count
from api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
        bookmarks_count=Count('bookmarks', distinct=True),
    )
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['created_at', 'likes_count',
                       'comments_count', 'bookmarks_count']
    filterset_fields = ['author__username']
    search_fields = ['caption', 'owner__username']

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
        bookmarks_count=Count('bookmarks', distinct=True),
    )
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['caption', 'owner__username']
    ordering_fields = ['created_at', 'likes_count', 'comments_count']
