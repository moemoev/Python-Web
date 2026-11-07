from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, file_size: int, message: str=None) -> None:
        self.file_size = file_size
        self.message = message

    @property
    def message(self):
        return self.__message

    