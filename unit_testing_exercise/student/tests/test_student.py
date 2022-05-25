from project.student import Student
from unittest import TestCase,main

class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Peter", {"Python Basics":["note1","note2"],"JS Basics":["note3","note4"]})
    def test_if_initiated_correctly_without_courses(self):
        name = "Peter"
        test_student = Student(name)
        self.assertEqual(name,test_student.name)
        self.assertEqual({},test_student.courses)

    def test_if_initiated_correctly_with_courses(self):
        name = "Peter"
        courses = {"Python Basics":["note1","note2"],"JS Basics":["note3","note4"]}
        test_student = Student(name,courses)
        self.assertEqual(name,test_student.name)
        self.assertEqual(courses,test_student.courses)

    def test_enrol_with_existing_course(self):
        course_name = "Python Basics"
        notes = ["new note"]
        res = self.student.enroll(course_name,notes)
        self.assertEqual("Course already added. Notes have been updated.",res)
        self.assertEqual(["note1","note2","new note"],self.student.courses[course_name])

    def test_enroll_new_course_with_notes(self):
        course_name = "Database Basics"
        notes = ["note 1","note 2"]
        res = self.student.enroll(course_name,notes,"Y")
        self.assertEqual({"Python Basics":["note1","note2"],"JS Basics":["note3","note4"],"Database Basics":["note 1","note 2"]},self.student.courses)
        self.assertEqual("Course and course notes have been added.",res)

    def test_enroll_new_course_with_notes_with_empty_string(self):
        course_name = "Database Basics"
        notes = ["note 1","note 2"]
        res = self.student.enroll(course_name,notes,"")
        self.assertEqual({"Python Basics":["note1","note2"],"JS Basics":["note3","note4"],"Database Basics":["note 1","note 2"]},self.student.courses)
        self.assertEqual("Course and course notes have been added.",res)

    def test_enroll_new_course_without_notes(self):
        course_name = "Database Basics"
        notes = ["note 1", "note 2"]
        res = self.student.enroll(course_name, notes, "N")
        self.assertEqual({"Python Basics": ["note1", "note2"], "JS Basics": ["note3", "note4"],
                          "Database Basics": []}, self.student.courses)
        self.assertEqual("Course has been added.", res)

    def test_add_notes_existing_course(self):
        note = "new note"
        course = "Python Basics"
        res = self.student.add_notes(course,note)
        self.assertEqual(["note1","note2","new note"],self.student.courses[course])
        self.assertEqual("Notes have been updated",res)

    def test_add_notes_exception_throw_if_course_not_in_courses(self):
        course_name = "Database Basics"
        notes = "note 1"
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name,notes)

        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))
        self.assertEqual({"Python Basics":["note1","note2"],"JS Basics":["note3","note4"]},self.student.courses)

    def test_leave_course_with_existing_course(self):
        course_name = "Python Basics"
        res = self.student.leave_course(course_name)
        self.assertEqual({"JS Basics":["note3","note4"]},self.student.courses)
        self.assertEqual("Course has been removed",res)

    def test_leave_course_throw_exception_with_non_existing_course(self):
        course_name = "Database Basics"
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course_name)
        self.assertEqual({"Python Basics":["note1","note2"],"JS Basics":["note3","note4"]},self.student.courses)
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))

if __name__ == "__main__":
    main()