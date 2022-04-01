from django.urls import include, path

from .views import MatchAPICreate, UserAPICreate


urlpatterns = [
               path('clients/create/', UserAPICreate.as_view(), name='create'),
               path('clients/<int:id>/match', MatchAPICreate.as_view(), name='match'),
               path('auth/', include('djoser.urls.authtoken')),
               path('auth/', include('djoser.urls.jwt')),
]
