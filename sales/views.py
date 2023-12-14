from rest_framework import generics
from .models import Sales, ClosingSales
from .serializers import SalesSerializer, ClosingSalesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Sales views

class SalesListCreateView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

# ClosingSales views

class CustomClosingSalesCreateView(APIView):
    def get(self, request, *args, **kwargs):
        instances = ClosingSales.objects.all()
        serializer = ClosingSalesSerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Check if there is an existing record
        existing_instance = ClosingSales.objects.first()

        # If an existing record is found, update it
        if existing_instance:
            return self.update_existing_instance(existing_instance, request, *args, **kwargs)
        # If no existing record is found, create a new one
        else:
            return self.create_new_instance(request, *args, **kwargs)

    def update_existing_instance(self, instance, request, *args, **kwargs):
        serializer = ClosingSalesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_new_instance(self, request, *args, **kwargs):
        serializer = ClosingSalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)