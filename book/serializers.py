from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password'
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        return user


# წიგნის მონაცემები
class BookSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Book

        fields = [
            'id',
            'username',
            'title',
            'author',
            'description',
            'published_year',
            'created_at'
        ]

        read_only_fields = [
            'id',
            'username',
            'created_at'
        ]