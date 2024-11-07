# Student Profile Summarization API

This project is a FastAPI-based RESTful API designed for managing and summarizing student profiles. It provides CRUD operations for handling student data and can generate concise profile summaries based on the provided details.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Add a Student](#add-a-student)
  - [Get All Students](#get-all-students)
  - [Get a Student by ID](#get-a-student-by-id)
  - [Update a Student](#update-a-student)
  - [Delete a Student](#delete-a-student)
  - [Get Student Profile Summary](#get-student-profile-summary)
- [Concurrency and Edge Case Handling](#concurrency-and-edge-case-handling)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- **CRUD Operations**: Easily add, retrieve, update, and delete student profiles.
- **Profile Summarization**: Generates concise summaries of student data using an LLM model.
- **Concurrency Handling**: Ensures safe updates through locking mechanisms.
- **Edge Case Management**: Validates inputs to handle edge cases, like negative or unrealistic ages and duplicate IDs.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Pipenv** (for managing virtual environments) or **pip**
- Basic knowledge of FastAPI

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ketanmehra003/FealtyX.git
    cd FealtyX
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the API Server**

    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### Add a Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Description**: Adds a new student profile to the database.

#### Request Body

```json
{
  "id": 1,
  "name": "Ketan Mehra",
  "age": 21,
  "email": "ketanmehra@example.com"
}
```
#### Response

```json
{
  "id": 1,
  "name": "Ketan Mehra",
  "age": 21,
  "email": "ketanmehra@example.com"
}
```

### Get All Students

- **Endpoint**: `/students`
- **Method**: `GET`
- **Description**: Retrieves all student profiles from the database.
#### Response

```json
[
  {
    "id": 1,
    "name": "Ketan Mehra",
    "age": 21,
    "email": "ketanmehra@example.com"
  },
  ...
]
```

### Get a Student by ID

- **Endpoint**: `/students/{student_id}`
- **Method**: `GET`
- **Description**: Retrieves the profile of a specific student by ID.
#### Response

```json
{
  "id": 1,
  "name": "Ketan Mehra",
  "age": 21,
  "email": "ketanmehra@example.com"
}
```

### Update a Student

- **Endpoint**: `/students/{student_id}`
- **Method**: `PUT`
- **Description**: Updates the details of a specific student by ID.

#### Request Body

```json
{
  "name": "Ketan Mehra",
  "age": 21,
  "email": "ketanmehra1@example.com"
}
```
#### Response

```json
{
  "id": 1,
  "name": "Ketan Mehra",
  "age": 21,
  "email": "ketanmehra1@example.com"
}
```

### Delete a Student

- **Endpoint**: `/students/{student_id}`
- **Method**: `DELETE`
- **Description**: Deletes a student profile by ID.
#### Response

```json
{
  "message": "Student deleted successfully."
}
```

### Get Student Profile Summary

- **Endpoint**: `/students/{student_id}/summary`
- **Method**: `GET`
- **Description**: Generates a brief summary of the student’s profile based on the provided details.
#### Response

```json
{
  "summary": "John Doe is a 20-year-old individual with an active email address."
}
```

## Concurrency and Edge Case Handling

### Concurrency Handling
- The `update` and `delete` operations use a thread lock to prevent race conditions when multiple requests try to modify the same record simultaneously.

### Edge Case Handling
- **Negative or Zero Age**: Input validation ensures that unrealistic ages are not accepted.
- **Duplicate IDs**: Attempting to add a student with an existing ID will result in a `400` error.
- **Boundary Values**: The system handles minimum and maximum allowable age values effectively.

## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **LangChain & LLMs**: For generating summaries based on student data.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Pydantic**: Data validation and parsing.
