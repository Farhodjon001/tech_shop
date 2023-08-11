from django.shortcuts import render
from .models import PcModel,Payment
from .serializers import PcSerializers,PaymentSerializers
from rest_framework import generics
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response


# Create your views here.

class PcListCreateApiView(generics.ListCreateAPIView):
    queryset = PcModel.objects.all()
    serializer_class =PcSerializers

class PcDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PcModel.objects.all()
    serializer_class = PcSerializers

class PaymentListCreateApiView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class PaymentDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class GetSoldPcApiView(APIView):
    def get(self,request,day):
        # day=request.query_params.get("day")
        data=datetime.strptime(day,'%Y-%m-%d').date()
        sold=PcModel.objects.filter(date__date=data).select_related('payment')
        serializer=PcSerializers(sold,many=True)
        return Response(serializer.data)



