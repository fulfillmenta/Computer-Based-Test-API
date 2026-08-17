from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.quiz_routes import router as quiz_router
from routes.admin_routes import router as admin_router
from routes.book_routes import router as book_router

app = FastAPI(title='Computer Based Test API', description='This app is built to help users practice for test and exams', version='1.0.0')

@app.get("/")
def home():
    return {'message': 'Computer Based Test API is running successfully!!!'}


app.include_router(auth_router)
app.include_router(quiz_router)
app.include_router(admin_router)
app.include_router(book_router)



