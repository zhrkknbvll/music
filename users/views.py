from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Регистрация нового пользователя"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)