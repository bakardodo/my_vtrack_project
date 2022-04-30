from django.core.exceptions import ValidationError


def only_letters(value):
    for val in value:
        if not val.isalpha():
            raise ValidationError('Name must be in letters only!')
