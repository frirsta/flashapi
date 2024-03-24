from django.db import IntegrityError
from rest_framework import serializers
from .models import Likes


class LikesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('You already liked this post.')
