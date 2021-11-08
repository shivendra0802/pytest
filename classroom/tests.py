from django.test import TestCase
from classroom.models import Student

class TestStudent(TestCase):

    # def setUp():
    #     student1 = Student.objects.create(
    #         first_name = "harry",
    #         last_name = "kumar",
    #         admission_number=1234
    #     )
    #     student_result = Student.objects.last()


    def student_can_be_created(self):
        student1 = Student.objects.create(
            first_name = "harry",
            last_name = "kumar",
            admission_number=1234
        )
        student_result = Student.objects.last() ### getting the last
        self.assertEqual(student_result.first_name,"harry")

    # def test_str_return(self):