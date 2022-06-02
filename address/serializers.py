from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


from address.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

