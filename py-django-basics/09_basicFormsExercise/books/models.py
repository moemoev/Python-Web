from django.db import models
from django.utils.text import slugify

from .mixins import TimestampMixin
from . import choices

class Book(TimestampMixin):
    title = models.CharField(
    max_length=100,
    unique=True,
)
    publisher = models.CharField(
    max_length=100,
)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,
    )
    genre = models.CharField(
        choices=choices.GenreChoices,
        default=choices.GenreChoices.OT,
    )
    language = models.CharField(
        choices=choices.LanguageChoices,
        default=choices.LanguageChoices.OT,
    )
    pages = models.PositiveIntegerField()
    is_available = models.BooleanField(
        default=True,
    )
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(
        unique=True,
    )

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tags(models.Model):
    name = models.CharField(
        max_length=50,
    )
    books = models.ManyToManyField(
        Book,
    )

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name