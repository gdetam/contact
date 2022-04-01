from dotenv import find_dotenv, load_dotenv

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import CustomUser, UsersLikes
from .serializers import UserLikeSerializer, UserRegistrationSerializer
from .utils import send_message


load_dotenv(find_dotenv())


class UserAPICreate(generics.CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer


class MatchAPICreate(generics.ListCreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLikeSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        user_like = get_object_or_404(
            CustomUser.objects.filter(id=self.kwargs.get('id'))
        )

        if user_like == user:
            return Response({'error': 'Нельзя лайкать самого себя'})
        if UsersLikes.objects.filter(user=user, user_like=user_like) is not None:
            return Response({'error': 'Уже лайкал(а)'})
        like = UsersLikes(user=user, user_like=user_like)
        like.save()
        if UsersLikes.objects.filter(user=user_like,
                                     user_like=user).exists():
            send_message(user, user_like)
            send_message(user_like, user)
        return Response({'like': 'Лайк отправлен!'}, status=status.HTTP_201_CREATED)
