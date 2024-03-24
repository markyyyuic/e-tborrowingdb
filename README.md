# Activity Setup Guide

This guide provides step-by-step instructions to set up a project with Miniconda, FastAPI, and a MySQL database.

## 1. Setup Miniconda

### 1.1 Download and Install Miniconda
- Download Miniconda from [Miniconda Website](https://docs.conda.io/en/latest/miniconda.html)
- Follow installation instructions for your operating system.
- Once installed, open the Miniconda Command Prompt

![Demo Preview](https://raw.githubusercontent.com/cbatuic/demo_fastapi/main/fastapi_demo_1_1_1.png)

### 1.2 Create Conda Python Environment
```bash
conda create --name your_env_name python=3.9
```

### 1.3 Activate Conda Python Environment
```bash
conda activate your_env_name
```

## 2. Setup FastAPI and its Dependencies

### 2.1 Install FastAPI, Uvicorn, and MySQL Connector
```bash
pip install fastapi uvicorn mysql-connector-python
```
> This Python code is using the pip package manager to install three Python packages: fastapi, uvicorn, and mysql-connector-python. Here's a breakdown of each package:

>> FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

>> Uvicorn: Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server that is used to run FastAPI applications. It provides fast performance and supports asynchronous code.

>> mysql-connector-python: This package is a MySQL database connector for Python. It allows Python programs to connect to and interact with MySQL databases.

By running this command, you're installing these packages, making them available for use in your Python environment.
### 2.2 Run FastAPI
```bash
uvicorn main:app --reload
```

## 3. Setup Database Environment

### 3.1 Download and Install XAMPP
- Download XAMPP from XAMPP Website
- Follow installation instructions for your operating system.

### 3.2 Create Database using PhpMyAdmin
- Open PhpMyAdmin and create a new database.

### 3.3 Create Table "users" with Three Columns
- id: Primary Key, Auto Increment
- username: VARCHAR(50)
- password: VARCHAR(255)

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    profile_image BLOB,
    UNIQUE KEY (username),
    UNIQUE KEY (email)
);


INSERT INTO users (username, password, email, profile_image)
VALUES
('user1', PASSWORD('password1'), 'user1@example.com', 'Profile 1 Lorem ipsum'),
('user2', PASSWORD('password2'), 'user2@example.com', 'Profile 2 Lorem ipsum'),
('user3', PASSWORD('password3'), 'user3@example.com', 'Profile 3 Lorem ipsum'),
('user4', PASSWORD('password4'), 'user4@example.com', 'Profile 4 Lorem ipsum'),
('user5', PASSWORD('password5'), 'user5@example.com', 'Profile 5 Lorem ipsum');

```

![Demo Preview](https://raw.githubusercontent.com/cbatuic/demo_fastapi/main/fastapi_demo_3_3_1.png)

### 3.4 Insert Dummy Users Data (At Least 5 Records)

![Demo Preview](https://raw.githubusercontent.com/cbatuic/demo_fastapi/main/fastapi_demo_3_4_1.png)

## 4. Setup FastAPI Routers for Table Users

### 4.1 Clone GitHub Repository
```bash
git clone https://github.com/cbatuic/demo_fastapi.git
```

### 4.2 Verify Database Configuration in models/db.py
```python
# model/db.py
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "your_db_name_here",
    "port": 3306,
}
```

# 5. Test the FastAPI Routers

## 5.1 Run FastAPI
```bash
uvicorn main:app --reload
```

## 5.2 Open FastAPI Docs in Browser
- Visit http://127.0.0.1:8000/docs

### 5.3 Try It Out! /api/users Route
- See Demo Preview
  
### 5.4 Try It Out! /api/users/{user_id}
- See Demo Preview

Done. Great Job! 🎉

# Demo Preview

![Demo Preview](https://raw.githubusercontent.com/cbatuic/demo_fastapi/main/fastapi_demo_preview.gif)


