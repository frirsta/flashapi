from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('user__posts', distinct=True),
        follower_count=Count('user__follower', distinct=True),
        following_count=Count('user__following', distinct=True),
    )
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['posts_count', 'follower_count', 'following_count']
    filterset_fields = ['user__username']
    search_fields = ['user__username']


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('user__posts', distinct=True),
        follower_count=Count('user__follower', distinct=True),
        following_count=Count('user__following', distinct=True),
    )
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
