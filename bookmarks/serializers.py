from rest_framework import serializers
from .models import Bookmarks
from django.db import IntegrityError


class BookmarksSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmarks
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                'You already bookmarked this post.')
