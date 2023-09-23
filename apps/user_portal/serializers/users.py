from rest_framework import serializers

from apps.user_portal.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GetUserSerializer(serializers.ModelSerializer):
    """
    Farm One Serializer
    """
    class Meta:
        model = User
        exclude = ('created_at', 'updated_at')

class PostUserSerializer(GetUserSerializer):
    pass

class PutUserSerializer(GetUserSerializer):
    pass

class PatchUserSerializer(GetUserSerializer):
    pass

class ListUserSerializer(GetUserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')