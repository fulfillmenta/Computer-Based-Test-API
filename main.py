import os
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router as auth_router
from routes.quiz_routes import router as quiz_router
from routes.admin_routes import router as admin_router
from routes.book_routes import router as book_router
from utilities.json_handler import load_json, append_json
from utilities.security import hash_password

app = FastAPI(title='Computer Based Test API', description='This app is built to help users practice for test and exams', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_default_admin():
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if not admin_username or not admin_password:
        return

    users = load_json("data_storage/users.json")
    already_exists = any(user["username"] == admin_username for user in users)

    if not already_exists:
        new_admin = {
            "id": str(uuid.uuid4()),
            "first_name": "Admin",
            "last_name": "Account",
            "date_of_birth": "1990-01-01",
            "email": "admin@example.com",
            "username": admin_username,
            "password_hash": hash_password(admin_password),
            "role": "admin",
        }
        append_json("data_storage/users.json", new_admin)
        print(f"Default admin '{admin_username}' created.")


@app.get("/")
def home():
    return {'message': 'Computer Based Test API is running successfully!!!'}


app.include_router(auth_router)
app.include_router(quiz_router)
app.include_router(admin_router)
app.include_router(book_router)