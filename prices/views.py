from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Price
from .serializers import PriceSerializer

class PriceList(APIView):
    def get(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data)

    def post(self, request):
        prices = Price.objects.all()
        if not prices:
            serializer = PriceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            price = prices[0]
            serializer = PriceSerializer(price, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceDetail(APIView):
    def get_object(self, pk):
        try:
            return Price.objects.get(pk=pk)
        except Price.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        price = self.get_object(pk)
        serializer = PriceSerializer(price)
        return Response(serializer.data)

    def put(self, request, pk):
        price = self.get_object(pk)
        serializer = PriceSerializer(price, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        price = self.get_object(pk)
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
