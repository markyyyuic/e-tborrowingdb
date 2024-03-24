# model/users.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
import bcrypt

UsersRouter = APIRouter(tags=["Administrator"])

# CRUD operations

@UsersRouter.get("/users/", response_model=list)
async def read_users(
    db=Depends(get_db)
):
    query = "SELECT admin_User, admin_Password FROM administrator"
    db[0].execute(query)
    users = [{"admin_User": user[0], "admin_Passowrd": user[1]} for user in db[0].fetchall()]
    return users

@UsersRouter.get("/users/{user_id}", response_model=dict)
async def read_user(
    user_id: int, 
    db=Depends(get_db)
):
    query = "SELECT id, username FROM users WHERE id = %s"
    db[0].execute(query, (user_id,))
    user = db[0].fetchone()
    if user:
        return {"id": user[0], "username": user[1]}
    raise HTTPException(status_code=404, detail="User not found")

@UsersRouter.post("/users/", response_model=dict)
async def create_user(
    email: str = Form(...), 
    username: str = Form(...), 
    password: str = Form(...), 
    db=Depends(get_db)
):
    # Hash the password using bcrypt
    hashed_password = hash_password(password)

    query = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
    db[0].execute(query, (email, username, hashed_password))

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_user_id = db[0].fetchone()[0]
    db[1].commit()

    return {"id": new_user_id, "username": username}

@UsersRouter.put("/users/{user_id}", response_model=dict)
async def update_user(
    user_id: int,
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    # Hash the password using bcrypt
    hashed_password = hash_password(password)

    # Update user information in the database 
    query = "UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s"
    db[0].execute(query, (email, username, hashed_password, user_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "User updated successfully"}
    
    # If no rows were affected, user not found
    raise HTTPException(status_code=404, detail="User not found")

@UsersRouter.delete("/users/{user_id}", response_model=dict)
async def delete_user(
    user_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT id FROM users WHERE id = %s"
        db[0].execute(query_check_user, (user_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        query_delete_user = "DELETE FROM users WHERE id = %s"
        db[0].execute(query_delete_user, (user_id,))
        db[1].commit()

        return {"message": "User deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()

# Password hashing function using bcrypt
def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string for storage
