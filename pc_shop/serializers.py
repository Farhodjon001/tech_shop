from rest_framework import serializers
from .models import PcModel,Payment

class PcSerializers(serializers.ModelSerializer):

    class Meta:
        model=PcModel
        fields=("id","model","protcessor",'ram','ssd','hdd')

class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model=Payment
        fields=('id','pc_id',"amount","unit_price",'price')