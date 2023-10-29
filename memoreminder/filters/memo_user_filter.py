import django_filters

from memoreminder.models import MemoUser


class MemoUserFilter(django_filters.FilterSet):
    class Meta:
        model = MemoUser
        fields = {
            'id': ['exact', 'in'],
            'username': ['exact', 'contains', 'in'],
            'first_name': ['exact', 'contains', 'in'],
            'last_name': ['exact', 'contains', 'in'],
            'created': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'modified': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }
