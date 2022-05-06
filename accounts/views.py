from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer


class AccountView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_user = User.objects.filter(username=serializer.validated_data['username']).exists()

        if find_user == True:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        user = User.objects.create_user(**serializer.validate_data)

        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)