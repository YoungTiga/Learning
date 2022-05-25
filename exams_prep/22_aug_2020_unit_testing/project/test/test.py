from project.student_report_card import StudentReportCard
from unittest import TestCase,main

class TestStudentReportCard(TestCase):

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("Pesho", 12)
        self.student_report_card.grades_by_subject = {"Math":[6]}

    def test_init(self):
        student_report_card = StudentReportCard("Pesho", 12)
        self.assertEqual("Pesho",student_report_card.student_name)
        self.assertEqual(12,student_report_card.school_year)
        self.assertEqual({},student_report_card.grades_by_subject)

    def test_student_name_setter_error_if_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 12)
        self.assertEqual("Student Name cannot be an empty string!",str(ex.exception))

    def test_student_name_setter_ok(self):
        self.student_report_card.student_name = "Ivan"
        self.assertEqual("Ivan",self.student_report_card.student_name)

    def test_school_year_setter_error_if_number_less_than_one(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Pesho", 0)
        self.assertEqual("School Year must be between 1 and 12!",str(ex.exception))

    def test_school_year_setter_error_if_number_greater_than_twelve(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Pesho", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_ok(self):
        self.student_report_card.school_year = 1
        self.assertEqual(1,self.student_report_card.school_year)


    def test_school_year_setter_error_if_number_is_negative(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Pesho", -13)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_with_non_existing_subject(self):
        self.student_report_card.add_grade("Geography",6)
        self.assertEqual({"Math":[6],"Geography":[6]},self.student_report_card.grades_by_subject)

    def test_grades_by_subject(self):
        expected = [6]
        self.assertEqual(expected,self.student_report_card.grades_by_subject["Math"])



    def test_add_grade_with_existing_subject(self):
        self.student_report_card.add_grade("Math",5)
        self.assertEqual({"Math":[6,5]},self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject(self):
        res = self.student_report_card.average_grade_by_subject()
        expected = "Math: 6.00"
        self.assertEqual(expected,res)

    def test_average_grade_for_all_subjects(self):
        res = self.student_report_card.average_grade_for_all_subjects()
        expected = "Average Grade: 6.00"
        self.assertEqual(expected, res)

    def test_repr_method(self):
        self.student_report_card.add_grade("S",6)
        expected="Name: Pesho\n"
        expected+= "Year: 12\n"
        expected+= "----------\n"
        expected+= "Math: 6.00\n"
        expected+= "S: 6.00\n"
        expected+= "----------\n"
        expected+= "Average Grade: 6.00"
        res = repr(self.student_report_card)
        self.assertEqual(expected,res)

if __name__=="__main__":
    main()