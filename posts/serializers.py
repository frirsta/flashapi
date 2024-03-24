from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.avatar.url')

    def validate_image(self, value):
        if value.size > 2*1024*1024:
            raise serializers.ValidationError(
                'Image size must be less than 2MB')
        if value.image.width > 1000 or value.image.height > 1000:
            raise serializers.ValidationError(
                'Image dimensions must be less than 1000x1000')
        return value

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user

    class Meta:
        model = Post
        fields = '__all__'
