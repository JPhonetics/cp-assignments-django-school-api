from django.core.exceptions import ValidationError
import re
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_name_format(val: str):
    good_input = re.fullmatch(r'[A-Za-z]+ [A-Za-z]\. [A-Za-z]+', val)
    if not good_input:
        raise ValidationError(
            message='Name must be in the format "First Middle Initial. Last"'
        )

def validate_school_email(val: str):
    if not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@school\.com$', val):
        raise ValidationError(
            message='Invalid school email format. Please use an email ending with "@school.com".'
        )

def validate_combination_format(val: str):
    good_combo = re.fullmatch(r'^[0-9]{2}-[0-9]{2}-[0-9]{2}', val)
    if not good_combo:
        raise ValidationError(
            message='Combination must be in the format "12-12-12"'
        )