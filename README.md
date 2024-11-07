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
    git clone https://github.com/your-username/student-profile-api.git
    cd student-profile-api
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

2. **Access the Documentation**

   Once the server is running, go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the interactive API documentation.

## API Endpoints

### Add a Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Description**: Adds a new student profile to the database.

#### Request Body

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 20,
  "email": "johndoe@example.com"
}
