from django.db import models
from .import choices

class Review(models.Model):
    author = models.CharField(
        max_length=100,
    )
    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    is_verified = models.BooleanField(
        default=False,
    )
    review_type = models.CharField(
        choices=choices.ReviewTypeChoices,
        default=choices.ReviewTypeChoices.OT,
    )
    book = models.ForeignKey(
        'books.Book',
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    is_spoiler = models.BooleanField(
        default=False,
    )