from django.db import models

# Create your models here.
class Student(models.Model):
    name: str = models.CharField()
    student_email: str = models.EmailField(
        max_length=254,
        unique=True
        )
    personal_email: str = models.EmailField(
        max_length=254,
        null=True,
        unique=True
        )
    locker_number: int = models.IntegerField(
        default=110,
        unique=True
    )
    locker_combination: str = models.CharField(
        default="12-12-12"
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