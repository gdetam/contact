from django_filters import rest_framework as filters

from users.models import CustomUser


class UserListFilter(filters.FilterSet):

    first_name = filters.CharFilter(field_name='first_name',
                                    lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='last_name',
                                   lookup_expr='icontains')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'sex']
