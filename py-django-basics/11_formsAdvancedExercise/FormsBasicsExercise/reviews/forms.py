from django import forms
from django.core.exceptions import ValidationError
from psycopg2._psycopg import Decimal

from FormsBasicsExercise.mixins import DisabledFormMixin
from reviews.models import Review


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def clean_rating(self) -> Decimal:
        rating = self.cleaned_data['rating']

        if not 0 < rating < 5:
            raise ValidationError("Rating must be between 0 and 5!")

        return rating

    def clean(self) -> dict:
        cleaned_data = self.cleaned_data

        if cleaned_data.get('is_spoiler') and not cleaned_data.get('body'):
            self.add_error("body", "markings as spoiler must include a body")
            self.add_error('is_spoiler', "marking  as spoiler without description is not ok buddy")

        return cleaned_data

class ReviewCreateForm(ReviewBaseForm):
    ...


class ReviewEditForm(ReviewBaseForm):
    ...


class ReviewDeleteForm(DisabledFormMixin, ReviewBaseForm):
    ...
