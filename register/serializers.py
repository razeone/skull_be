from register.models import Customer

from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'url',
            'user_id',
            'email',
            'date_joined',
            'date_of_birth')
