# main.py
from fastapi import FastAPI
from model.users import UsersRouter
from model.categories import students
from model.expenses import ExpensesRouter

app = FastAPI()

# Include CRUD routes from modules

app.include_router(students, prefix="/api")
