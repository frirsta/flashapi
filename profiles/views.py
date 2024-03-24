from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('user__post', distinct=True),
        follower_count=Count('user__follower', distinct=True),
        following_count=Count('user__following', distinct=True),
    )
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['post_count', 'follower_count', 'following_count']
    filterset_fields = ['user__username']
    search_fields = ['user__username']


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('user__post', distinct=True),
        follower_count=Count('user__follower', distinct=True),
        following_count=Count('user__following', distinct=True),
    )
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
