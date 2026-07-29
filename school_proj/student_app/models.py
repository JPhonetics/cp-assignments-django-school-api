from django.db import models

# Create your models here.
class Student(models.Model):
    name: str = models.CharField()
    student_email: str = models.EmailField(
        max_length=254
        )
    personal_email: str = models.EmailField(
        max_length=254,
        null=True
        )
    locker_number: int = models.IntegerField()
    locker_combination: str = models.CharField()
    good_student: bool = models.BooleanField(
        default=False
        )