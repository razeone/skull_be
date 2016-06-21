from register.models import Customer
from rest_framework import viewsets
from register.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-date_joined')
    serializer_class = CustomerSerializer
