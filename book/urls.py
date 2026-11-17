from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    BookListCreateView,
    BookDetailView
)


urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
        "book/",
        BookListCreateView.as_view(),
        name="book-list-create"
    ),

    path(
        "book/<int:pk>/",
        BookDetailView.as_view(),
        name="book-detail"
    ),

]
