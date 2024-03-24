from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import Comments
from .serializers import CommentsSerializer
from api.permissions import IsOwnerOrReadOnly


class CommentsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
