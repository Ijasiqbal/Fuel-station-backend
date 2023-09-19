from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CreditTransaction
from .serializers import CreditTransactionSerializer

@api_view(['GET', 'POST'])
def credit_transaction_list(request):
    if request.method == 'GET':
        transactions = CreditTransaction.objects.all()
        serializer = CreditTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreditTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def credit_transaction_detail(request, pk):
    try:
        transaction = CreditTransaction.objects.get(pk=pk)
    except CreditTransaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreditTransactionSerializer(transaction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreditTransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
