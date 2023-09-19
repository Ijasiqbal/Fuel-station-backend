from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Creditor
from .serializers import CreditorSerializer

@api_view(['GET', 'POST'])
def creditor_list(request):
    if request.method == 'GET':
        creditors = Creditor.objects.all()
        serializer = CreditorSerializer(creditors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreditorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def creditor_detail(request, pk):
    try:
        creditor = Creditor.objects.get(pk=pk)
    except Creditor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreditorSerializer(creditor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreditorSerializer(creditor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        creditor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
