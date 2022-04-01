from django.urls import include, path

from .views import MatchAPICreate, UserAPICreate, UserListAPIFilter

urlpatterns = [
               path('clients/create/', UserAPICreate.as_view(), name='create'),
               path('clients/<int:id>/match', MatchAPICreate.as_view(), name='match'),
               path('list/', UserListAPIFilter.as_view(), name='list_filter'),
               path('auth/', include('djoser.urls.authtoken')),
               path('auth/', include('djoser.urls.jwt')),
]
