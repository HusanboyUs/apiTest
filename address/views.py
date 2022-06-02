from rest_framework import viewsets
from address.serializers import AddressSerializer
from address.models import Address
from rest_framework.response import Response
from rest_framework import status

class AddressViewSet(viewsets.ModelViewSet):
        queryset=Address.objects.all()
        serializer_class = AddressSerializer
        Response({'success': 'Data successfully submitted'}, status=status.HTTP_200_OK)

        def retrieve(self, request, *args, **kwargs):
            params=kwargs
            address=Address.objects.filter(city=params['pk'])
            serializer=AddressSerializer(address, many=True)
            return Response(serializer.data)

        def create(self, request, *args, **kwargs):
              pass    