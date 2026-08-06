from django.db import models
from django.core import validators as val
from .validators import validate_name_format
from .validators import validate_school_email
from .validators import validate_combination_format

# Create your models here.
class Student(models.Model):
    name: str = models.CharField(
        max_length=100,
        validators=[
            validate_name_format
        ]
    )
    student_email: str = models.EmailField(
        max_length=254,
        unique=True,
        validators=[
            validate_school_email
        ]
    )
    personal_email: str = models.EmailField(
        max_length=254,
        null=True,
        unique=True
    )
    locker_number: int = models.IntegerField(
        default=110,
        unique=True,
        validators=[
            val.MinValueValidator(1, "Ensure this value is greater than or equal to 1."),
            val.MaxValueValidator(200, "Ensure this value is less than or equal to 200.")
        ]
    )
    locker_combination: str = models.CharField(
        default="12-12-12",
        validators=[
            validate_combination_format
        ]
    )
    good_student: bool = models.BooleanField(
        default=True
    )
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, val: int):
        self.locker_number = int(val)
        self.save()
        
    def student_status(self, val: bool):
        self.good_student = bool(val)
        self.save()
        
    def clean(self):
        if self.student_email == self.personal_email:
            raise ValidationError(
                "Student email and personal email cannot be the same."
            )