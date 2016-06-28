from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from register.models import Customer
from register.utils import activate_user
from register.serializers import CustomerSerializer




class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-date_joined')
    serializer_class = CustomerSerializer


@api_view(['GET'])
def activate_user_view(request, id):
    result = activate_user(id)
    return Response(result, 200)
