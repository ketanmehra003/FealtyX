from pydantic import BaseModel, Field, EmailStr, field_validator

class Student(BaseModel):
    id: int
    name: str = Field(..., max_length=100, description="Name must be a string with a maximum length of 100 characters")
    age: int = Field(..., gt=0, le=100, description="Age must be a positive integer with constraints: 0 < age <= 100")
    email: EmailStr

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be a positive integer")
        return value

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: EmailStr | None = None
