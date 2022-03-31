from djoser.serializers import UserCreateSerializer

from .models import CustomUser
from .utils import add_watermark


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = ('avatar', 'sex', 'first_name',
                  'last_name', 'email') + ('password', )

    def create(self, validated_data):
        avatar = validated_data.pop('avatar')
        new_avatar = add_watermark(avatar)
        validated_data['avatar'] = new_avatar
        return super().create(validated_data)
