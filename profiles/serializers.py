from rest_framework import serializers
from .models import Profile
from followers.models import Followers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField(source='follower_count')
    following_count = serializers.ReadOnlyField(source='following_count')
    posts_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()

    def get_following_id(self, obj):
        """
        Retrieve the ID of the following relationship between the request user and the profile user.
        """
        request = self.context.get('request')
        try:
            return Followers.objects.get(user=request.user, followed=obj.user).id
        except Followers.DoesNotExist:
            return None

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the profile.
        """
        request = self.context.get('request')
        return obj.user == request.user

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'city', 'avatar', 'website', 'facebook',
                  'twitter', 'linkedin', 'github', 'date_joined', 'updated_on',
                  'is_owner', 'followers_count', 'following_count', 'posts_count', 'following_id']
