from django import forms

from basicFormsExercise.mixins import DisabledFormMixin
from .models import Book, Tags

# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget = forms.Textarea(
#             attrs={'placeholder':'e.g done'}
#         )
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#     )
#     isbn = forms.CharField(
#         max_length=13,
#    )

class BookFormBasic(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        abstract = True
        model = Book
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Insert title here'}),
        }


class BookCreateForm(BookFormBasic):
    field_order = [
        'isbn',
        'price',
        'title', # change order of  displayed fields
    ]

class BookEditForm(BookFormBasic):
    ...

class BookDeleteForm(DisabledFormMixin,BookFormBasic):
    ...

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
    )