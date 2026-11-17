from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Book


class BookAPITest(APITestCase):

    def setUp(self):
        # ჩვეულებრივი მომხმარებელი
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        # ადმინისტრატორი
        self.admin = User.objects.create_user(
            username="admin",
            password="adminpassword123",
            is_staff=True
        )

        # Token-ები
        self.user_token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin)

        self.book = Book.objects.create(
            user=self.admin,
            title="Python",
            author="John",
            description="Python programming book",
            published_year=2024
        )

    #  რეგისტრაციის ტესტი
    def test_register(self):
        response = self.client.post(
            "/api/register/",
            {
                "username": "newuser",
                "email": "new@example.com",
                "password": "newpassword123"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)

    #  Token-ით ავტორიზაციის ტესტი
    def test_login(self):
        response = self.client.post(
            "/api/login/",
            {
                "username": "testuser",
                "password": "testpassword123"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    #  წიგნების ნახვის ტესტი
    def test_get_books(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )

        response = self.client.get("/api/book/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #  წიგნის დამატების ტესტი
    def test_create_book(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )

        response = self.client.post(
            "/api/book/",
            {
                "title": "Django",
                "author": "James",
                "description": "Django REST Framework",
                "published_year": 2025
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    #  ჩვეულებრივი მომხმარებელი ვერ წაშლის წიგნს
    def test_user_cannot_delete_book(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )

        response = self.client.delete(
            f"/api/book/{self.book.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #  ადმინისტრატორს შეუძლია წიგნის წაშლა
    def test_admin_can_delete_book(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.admin_token.key}"
        )

        response = self.client.delete(
            f"/api/book/{self.book.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)