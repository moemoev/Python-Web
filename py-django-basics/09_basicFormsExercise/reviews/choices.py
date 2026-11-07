from django.db import models

class ReviewTypeChoices(models.TextChoices):
    TXT = "text", "Text"
    VID = "video", "Video"
    AUD = "audio", "Audio"
    OT = "other", "Other"

