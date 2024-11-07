from typing import Dict
from models import Student

students_db: Dict[int, Student] = {}

def get_student(student_id: int) -> Student | None:
    return students_db.get(student_id)

def add_student(student: Student):
    students_db[student.id] = student

def update_student(student_id: int, student_data: dict):
    if student_id in students_db:
        updated_data = students_db[student_id].model_copy(update=student_data)
        students_db[student_id] = updated_data

def delete_student(student_id: int):
    if student_id in students_db:
        del students_db[student_id]
