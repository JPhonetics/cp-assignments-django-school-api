from student_app.models import Student
from student_app.serializers import StudentSerializer

all_student = Student.objects.all()
ser_student = StudentSerializer(all_student, many=True)
print(ser_student.data)

dict_data={
    
}