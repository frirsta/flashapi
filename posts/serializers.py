from rest_framework import serializers
from .models import Post
from likes.models import Likes
from bookmarks.models import Bookmarks


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    likes_id = serializers.SerializerMethodField()
    bookmarks_id = serializers.SerializerMethodField()
    bookmarks_count = serializers.ReadOnlyField()
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

    def get_likes_id(self, obj):
        request = self.context.get('request')
        try:
            like_instance = Likes.objects.get(owner=request.user, post=obj)
            return like_instance.id
        except Likes.DoesNotExist:
            return None

    def get_bookmarks_id(self, obj):
        request = self.context.get('request')
        try:
            bookmark_instance = Bookmarks.objects.get(
                owner=request.user, post=obj)
            return bookmark_instance.id
        except Bookmarks.DoesNotExist:
            return None

    class Meta:
        model = Post
        fields = ['id', 'author', 'caption', 'image', 'date_posted', 'updated', 'owner',
                  'is_owner', 'comments_count', 'likes_count', 'likes_id', 'bookmarks_id',
                  'bookmarks_count', 'profile_id', 'profile_image']
        extra_kwargs = {"author": {"write_only": True}}
