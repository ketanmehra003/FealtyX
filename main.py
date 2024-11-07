from fastapi import FastAPI, HTTPException, status
from models import Student, StudentUpdate
from database import students_db, add_student, get_student, update_student, delete_student
from llama import get_student_summary
import threading

app = FastAPI()
lock = threading.Lock()

@app.post("/students", response_model=Student)
def create_student(student: Student):
    with lock:
        if student.id in students_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Student with this ID already exists."
            )
        try:
            add_student(student)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to add student: {e}"
            )
    return student

@app.get("/students", response_model=list[Student])
def get_all_students():
    try:
        return list(students_db.values())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve students: {e}"
        )

@app.get("/students/{student_id}", response_model=Student)
def get_student_by_id(student_id: int):
    try:
        student = get_student(student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found."
            )
        return student
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve student: {e}"
        )

@app.put("/students/{student_id}", response_model=Student)
def update_student_by_id(student_id: int, student_data: StudentUpdate):
    with lock:
        try:
            student = get_student(student_id)
            if not student:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Student not found."
                )
            update_student(student_id, student_data.model_dump(exclude_unset=True))
            return students_db[student_id]
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update student: {e}"
            )

@app.delete("/students/{student_id}")
def delete_student_by_id(student_id: int):
    with lock:
        try:
            if student_id not in students_db:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Student not found."
                )
            delete_student(student_id)
            return {"message": "Student deleted successfully."}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to delete student: {e}"
            )

@app.get("/students/{student_id}/summary")
def get_student_summary_by_id(student_id: int):
    try:
        student = get_student(student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found."
            )
        try:
            summary = get_student_summary(student.model_dump())
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to generate student summary: {e}"
            )
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"This functionality is currently unavailable in this environment as it requires an Ollama setup. Please refer to the demo video for a demonstration."
        )
