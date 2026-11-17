from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from drf_spectacular.utils import extend_schema

from .models import Book
from .serializers import RegisterSerializer, BookSerializer
from .permissions import IsAdminOrReadOnly

class RegisterView(APIView):

    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Authentication"],
        summary="Register a new user",
        request=RegisterSerializer
    )
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(
                user=user
            )

            return Response({
                "message": "Registration successful",
                "username": user.username,
                "email": user.email,
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Authentication"],
        summary="Login and get token",
        request=AuthTokenSerializer
    )
    def post(self, request):

        serializer = AuthTokenSerializer(
            data=request.data
        )

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            token, created = Token.objects.get_or_create(
                user=user
            )

            return Response({
                "message": "Login successful",
                "username": user.username,
                "token": token.key
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all().order_by("-id")
    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly
    ]

    @extend_schema(
        tags=["Books"],
        summary="Get all books"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Books"],
        summary="Create a new book"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly
    ]

    @extend_schema(
        tags=["Books"],
        summary="Get one book"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Books"],
        summary="Update book"
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Books"],
        summary="Partially update book"
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Books"],
        summary="Delete book"
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
