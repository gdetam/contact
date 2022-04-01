from django_filters.rest_framework import DjangoFilterBackend

from dotenv import find_dotenv, load_dotenv

from geopy.distance import great_circle

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import UserListFilter
from .models import CustomUser, UsersLikes
from .serializers import UserLikeSerializer, \
                         UserListSerializer, \
                         UserRegistrationSerializer
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
        if UsersLikes.objects.filter(user=user,
                                     user_like=user_like) is not None:
            return Response({'error': 'Уже лайкал(а)'})
        like = UsersLikes(user=user, user_like=user_like)
        like.save()
        if UsersLikes.objects.filter(user=user_like,
                                     user_like=user).exists():
            send_message(user, user_like)
            send_message(user_like, user)
        return Response({'like': 'Лайк отправлен!'}, status=status.HTTP_201_CREATED)


class UserListAPIFilter(generics.ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = UserListFilter

    def list(self, request, *args, **kwargs):
        if self.request.query_params.get('distance'):
            distance = self.request.query_params.get('distance')
            p1 = (self.request.user.latitude, self.request.user.longitude)
            users = []
            users_from_queryset = CustomUser.objects.all()
            for user in users_from_queryset:
                p2 = (user.latitude, user.longitude)
                way = great_circle(p1, p2).meters
                if int(distance) >= int(round(way)):
                    users.append(user)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)
        return Response({'error': 'Укажите дистанцию!'})
