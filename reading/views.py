from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reading
from .serializers import ReadingSerializer

@api_view(['GET', 'POST'])
def reading_list(request):
    if request.method == 'GET':
        readings = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reading_detail(request, pk):
    try:
        reading = Reading.objects.get(pk=pk)
    except Reading.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReadingSerializer(reading)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReadingSerializer(reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
