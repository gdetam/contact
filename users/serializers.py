from djoser.serializers import UserCreateSerializer

from .models import CustomUser


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = ('avatar', 'sex', 'first_name',
                  'last_name', 'email') + ('password', )
