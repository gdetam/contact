from rest_framework import generics

from .models import CustomUser
from .serializers import UserRegistrationSerializer


class UserAPICreate(generics.CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
