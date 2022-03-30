from django.urls import include, path

from .views import UserAPICreate

urlpatterns = [
               path('clients/create/', UserAPICreate.as_view(), name='create'),
               path('auth/', include('djoser.urls.authtoken')),
               path('auth/', include('djoser.urls.jwt')),
]
