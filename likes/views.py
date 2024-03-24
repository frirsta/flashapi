from rest_framework import permissions, generics, filters
from .models import Likes
from .serializers import LikesSerializer
from api.permissions import IsOwnerOrReadOnly


class LikesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
