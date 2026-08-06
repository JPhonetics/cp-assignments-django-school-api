from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentAllSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = [
            'name', 
            'student_email', 
            'personal_email',
            'locker_number',
            'locker_combination',
            'good_student',
        ]

class StudentSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = [
            'name', 
            'student_email', 
            'locker_number', 
        ]
        # fields = '__all__'
        # exclude = ['personal_email']