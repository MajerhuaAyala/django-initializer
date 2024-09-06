from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from .application import get_user_by_query_name


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('id', None)
        user_name = request.query_params.get('username', None)

        user = get_user_by_query_name(user_id, user_name)

        if user is None:
            return Response({'error': 'User or name not found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(user)

        return Response(serializer.data)
