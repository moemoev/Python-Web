from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def bad_language_validation(value: str) -> None:
    words = ["badwords_1"]

    for word in words:
        if word in value:
            raise ValidationError("The function says, this is bad Language!")

@deconstructible
class BadLanguageValidator:
    BAD_WORDS = ["badwords_2"]

    def __init__(self, message):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not isinstance(value, str):
            raise ValueError("Message must be a string")

        if not value.strip():
            raise ValueError("Message can't be empty")


        self.__message = value

    def __call__(self,value: str,  *args, **kwargs):
        for word in self.BAD_WORDS:
            if word in value:
                raise ValidationError(self.message)
