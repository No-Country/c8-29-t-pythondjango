from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import JobSerializer


class JobApiView(APIView):
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

