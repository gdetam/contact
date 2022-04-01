from djoser.serializers import UserCreateSerializer

from rest_framework import serializers

from .models import CustomUser, UsersLikes
from .utils import add_watermark


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = ('avatar', 'sex', 'first_name',
                  'last_name', 'email', 'latitude', 'longitude') + ('password',)

    def create(self, validated_data):
        avatar = validated_data.pop('avatar')
        new_avatar = add_watermark(avatar)
        validated_data['avatar'] = new_avatar
        return super().create(validated_data)


class UserLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersLikes
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('sex', 'first_name',
                  'last_name', 'email', 'latitude', 'longitude')
