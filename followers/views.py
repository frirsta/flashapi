from api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowersSerializer
from rest_framework import generics, filters


class FollowersList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
