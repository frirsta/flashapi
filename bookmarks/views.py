from rest_framework import permissions, generics
from .models import Bookmarks
from .serializers import BookmarksSerializer
from api.permissions import IsOwnerOrReadOnly


class BookmarksList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarksDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer
