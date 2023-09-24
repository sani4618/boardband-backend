from rest_framework import serializers
from broadbandapp.models import BroadbandAppModel

class BroadbandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadbandAppModel
        fields =(
         'customerid',
         'customerName',
         'broadbandplan',
         'mobileNo',
         'subDate',
         'NxtSubDate',
         'amount',
         'address',
         'pincode',
         'ntwid'
    )