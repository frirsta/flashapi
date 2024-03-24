from rest_framework import serializers
from .models import Profile
from followers.models import Followers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()

    def get_following_id(self, obj):
        request = self.context.get('request')
        try:
            return Followers.objects.get(user=request.user, followed=obj.user).id
        except:
            return None

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.user == request.user

    class Meta:
        model = Profile
        fields = '__all__'
