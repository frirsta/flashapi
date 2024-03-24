from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(
        source='owner.profile.avatar.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    post = serializers.ReadOnlyField(source='post.id')

    def get_created_at(self, instance):
        return naturaltime(instance.created_at)

    def get_updated_at(self, instance):
        return naturaltime(instance.updated_at)

    def get_is_owner(self, instance):
        request = self.context.get('request')
        return instance.owner == request.user

    class Meta:
        model = Comments
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.id')
