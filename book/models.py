from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class Book(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books'
    )

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=150)

    description = models.TextField()

    published_year = models.PositiveIntegerField(validators=[MinValueValidator(1000),MaxValueValidator(3000)])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title