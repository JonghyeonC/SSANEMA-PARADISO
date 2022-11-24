from rest_framework import serializers
from .models import Community, Community_comment
from django.contrib.auth import get_user_model

class CommunitySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user',)


class CommunityCommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Community_comment
        fields = '__all__'
        read_only_fields = ('community',)