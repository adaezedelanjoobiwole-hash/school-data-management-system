from dataclasses import dataclass
from typing import Dict, List, Optional
import sys


@dataclass
class Teacher:
    name: str
    teacher_id: int
    subject: str

    def __str__(self) -> str:
        return f"Teacher ID: {self.teacher_id} | Name: {self.name} | Subject: {self.subject}"


@dataclass
class Student:
    name: str
    student_id: int
    grade_level: str
    major: str

    def __str__(self) -> str:
        return f"Student ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level} | Major: {self.major}"


class School:
    def __init__(self, school_name: str) -> None:
        self.school_name: str = school_name
        self.teachers: Dict[int, Teacher] = {}
        self.students: Dict[int, Student] = {}

    def add_teacher(self, teacher: Teacher) -> bool:
        if teacher.teacher_id in self.teachers:
            print(f"  ! Teacher ID '{teacher.teacher_id}' already exists.")
            return False
        self.teachers[teacher.teacher_id] = teacher
        return True

    def add_student(self, student: Student) -> bool:
        if student.student_id in self.students:
            print(f"  ! Student ID '{student.student_id}' already exists.")
            return False
        self.students[student.student_id] = student
        return True

    def display_teachers(self) -> None:
        print(f"\n**** Teachers at {self.school_name} ({len(self.teachers)}) ****")
        if not self.teachers:
            print("No teachers found.")
        else:
            for teacher in self.teachers.values():
                print(f"  {teacher}")

    def display_students(self) -> None:
        print(f"\n**** Students at {self.school_name} ({len(self.students)}) ****")
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(f"  {student}")


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  ! This field cannot be empty.")


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ! Please enter a valid integer ID.")


def run_menu() -> None:
    school = School("Springfield High School")
    
    school.add_teacher(Teacher("Dr. Smith", 101, "Mathematics"))
    school.add_teacher(Teacher("Ms. Davis", 102, "Physics"))
    school.add_student(Student("Alice Johnson", 1001, "11th", "Computer Science"))
    school.add_student(Student("Bob Brown", 1002, "12th", "Engineering"))

    while True:
        print("\n--- SCHOOL MANAGEMENT MENU ---")
        print("1. Add teacher")
        print("2. Add student")
        print("3. Show all teachers")
        print("4. Show all students")
        print("0. Exit")
        
        choice = input("Choose: ").strip()

        if choice == "1":
            name = read_non_empty("Teacher Name: ")
            tid = read_integer("Teacher ID (e.g. 103): ")
            subject = read_non_empty("Subject: ")
            if school.add_teacher(Teacher(name, tid, subject)):
                print("  Teacher added successfully.")
        elif choice == "2":
            name = read_non_empty("Student Name: ")
            sid = read_integer("Student ID (e.g. 1003): ")
            grade = read_non_empty("Grade Level (e.g. 10th): ")
            major = read_non_empty("Major/Programme: ")
            if school.add_student(Student(name, sid, grade, major)):
                print("  Student added successfully.")
        elif choice == "3":
            school.display_teachers()
        elif choice == "4":
            school.display_students()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("  ! Invalid choice. Please select between 0 and 4.")


if __name__ == "__main__":
    if "--menu" in sys.argv:
        run_menu()
    else:
        school = School("Springfield Academy")

        subjects: List[str] = ["Mathematics", "Physics", "Literature", "Chemistry"]
        grades: List[str] = ["9th Grade", "10th Grade", "11th Grade", "12th Grade"]
        majors: List[str] = ["Science", "Arts", "Computer Science", "Engineering"]

        for number in range(1, 6):
            subject = subjects[(number - 1) % len(subjects)]
            grade = grades[(number - 1) % len(grades)]
            major = majors[(number - 1) % len(majors)]

            school.add_teacher(Teacher(f"Teacher {number}", 100 + number, subject))
            school.add_student(Student(f"Student {number}", 1000 + number, grade, major))

        school.display_teachers()
        school.display_students()