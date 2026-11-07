from django.db import models

class GenreChoices(models.TextChoices):
    FI = "fiction", "Fiction"
    NON_FI = "non_fiction", "Non-Fiction"
    FA = "fantasy", "Fantasy"
    SCI = "science", "Science"
    OT = "other", "Other"
