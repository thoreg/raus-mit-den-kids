# -*- coding: utf-8 -*-
from rest_framework import permissions, viewsets
# from rest_framework.response import Response

from location.models import Address
from location.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    model = Address
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    '''
    def create(self, request):
        requester_id = request.POST.get('requester_id', None)
        environment_id = request.POST.get('environment_id', None)

        if not requester_id:
            return Response({'message': 'Requester ID invalid'},
                            status=status.HTTP_411_LENGTH_REQUIRED)

        if not environment_id:
            return Response({'message': 'Environment ID invalid'},
                            status=status.HTTP_411_LENGTH_REQUIRED)

        if Run.objects.filter(environment_id=environment_id, status=Status.RUNNING).exists():
            message = 'There is already a test execution running for this environment.'
            return Response({'message': message}, status=status.HTTP_409_CONFLICT)

        create_test_execution.delay(requester_id, environment_id)

        return Response({'message': 'Test execution successful'}, status=status.HTTP_200_OK)
    '''
