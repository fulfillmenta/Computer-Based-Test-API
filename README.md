Computer Based Test (CBT) API

A backend API built with FastAPI for a Computer-Based Test practice app, aimed at exams like JAMB. It supports user registration/login, role-based access (admin vs user), subject-based quizzes with scoring, and uploading/reading exam-relevant novels.

Live API: https://cbt-api-tauf.onrender.com Interactive API docs (Swagger UI): https://cbt-api-tauf.onrender.com/docs

Features
User registration and login with hashed passwords (bcrypt) and JWT-based authentication
Two roles: user (takes quizzes, reads books) and admin (manages questions, books, users)
Quiz system: pick 1–4 subjects, get matching questions (answers hidden), submit answers, get scored with a percentage
Quiz result history, per user and admin-wide
Admin question management (add, edit, delete)
Book upload/search/read feature — admins upload .txt novels (e.g. JAMB literature texts), users can search and read them by title
Data stored as JSON files and plain text files (no external database required)

Tech Stack
Python 3
FastAPI — web framework
Uvicorn — ASGI server
Pydantic — request/response validation
bcrypt — password hashing
PyJWT — authentication tokens
python-multipart — file upload support
python-dotenv — environment variable management

Project Structure
cbt_app/
├── main.py                  # App entry point, CORS setup, router registration
├── create_admin.py          # One-time script to create the first admin account
├── requirements.txt
│
├── routes/                  # HTTP endpoints (thin - delegate to services)
│   ├── auth_routes.py       # /register, /login
│   ├── quiz_routes.py       # /subjects, /quiz/start, /quiz/submit, /results/me
│   ├── admin_routes.py      # /admin/questions, /admin/users, /admin/results
│   └── book_routes.py       # /admin/books, /books, /books/search, /books/read
│
├── services/                 # Business logic
│   ├── auth_service.py
│   ├── quiz_service.py
│   ├── admin_service.py
│   └── book_service.py
│
├── models/                   # Pydantic request/response schemas
│   ├── user_info.py
│   ├── question_info.py
│   └── book_info.py
│
├── middleware/
│   └── auth_middleware.py   # Token verification, role-based access control
│
├── utilities/
│   ├── json_handler.py      # Read/write/append JSON files
│   ├── validators.py        # Input validation rules
│   └── security.py          # Password hashing, JWT creation/verification
│
└── data_storage/
    ├── users.json
    ├── questions.json
    ├── results.json
    ├── books.json
    └── uploaded_books/      # Uploaded .txt book files
Local Setup
Clone the repository
bash
   git clone https://github.com/fulfillmenta/Computer-Based-Test-API.git
   cd Computer-Based-Test-API
Create and activate a virtual environment
bash
   python3 -m venv venv
   source venv/bin/activate
Install dependencies
bash
   pip install -r requirements.txt
Set up environment variables Create a .env file in the project root:
   SECRET_KEY=your-own-random-secret-key

Generate a random key with:

bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
Create the data storage folders (if not already present)
bash
   mkdir -p data_storage/uploaded_books
Create your first admin account Edit the details inside create_admin.py, then run:
bash
   python3 create_admin.py
Run the server
bash
   uvicorn main:app --reload

API will be available at http://localhost:8000, with interactive docs at http://localhost:8000/docs.

Authentication

Most endpoints require a JWT token, obtained by logging in.

Call POST /login with a valid username and password.
Copy the access_token from the response.
Send it on every subsequent request as a header:
   Authorization: Bearer <your_token_here>

Tokens encode the user's id and role. Admin-only routes check the role and reject non-admins with a 403 Forbidden.

API Endpoints
Auth
Method	Endpoint	Auth required	Description
POST	/register	No	Register a new user (role defaults to user)
POST	/login	No	Log in, returns a JWT access token

POST /register — request body:

json
{
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1998-05-14",
  "email": "john@example.com",
  "username": "johnd",
  "password": "securepass123"
}

POST /login — request body:

json
{
  "username": "johnd",
  "password": "securepass123"
}

Response:

json
{
  "access_token": "eyJhbGciOi...",
  "role": "user"
}
Quiz (requires login)
Method	Endpoint	Auth required	Description
GET	/subjects	No	List available quiz subjects
POST	/quiz/start	Yes (any user)	Get quiz questions for 1–4 chosen subjects (answers hidden)
POST	/quiz/submit	Yes (any user)	Submit answers, get scored, result is saved
GET	/results/me	Yes (any user)	View your own past quiz results

POST /quiz/start — request body:

json
["maths", "chemistry"]

POST /quiz/submit — request body:

json
[
  {"question_id": "q001", "selected_answer": "56"},
  {"question_id": "q002", "selected_answer": "Water"}
]

Response:

json
{
  "score": 2,
  "total": 2,
  "percentage": "100.0%",
  "subjects": ["maths", "chemistry"]
}
Admin — Questions (requires admin role)
Method	Endpoint	Description
POST	/admin/questions	Add a new question
PUT	/admin/questions/{question_id}	Edit an existing question
DELETE	/admin/questions/{question_id}	Delete a question
GET	/admin/users	List all registered users
GET	/admin/results	View all quiz results (all users)

POST /admin/questions — request body:

json
{
  "subject": "maths",
  "question_text": "What is 7 x 8?",
  "options": ["54", "56", "58", "64"],
  "answer": "56"
}
Books
Method	Endpoint	Auth required	Description
POST	/admin/books	Admin only	Upload a .txt book (multipart form: title, author, category, file)
GET	/books	Any user	List all books
GET	/books/search?query=...	Any user	Search books by title/author
GET	/books/read?title=...	Any user	Read a book's full content by title
GET	/admin/books/{book_id}	Admin only	Read a book by its id
PUT	/admin/books/{book_id}	Admin only	Edit a book's title/author/category
DELETE	/admin/books/{book_id}	Admin only	Delete a book

Note: regular users never see a book's internal id — only admins do, since users read by title instead.

Testing

test.py at the project root contains scratch tests for the core utility and service functions (JSON handling, security, validators, auth, and quiz scoring). Run it with:

bash
python3 test.py
Notes on Data Storage

This project stores data as JSON files and plain text files rather than a database, for simplicity. data_storage/ is excluded from version control (see .gitignore) to avoid committing real user data or secrets. When deployed on a platform with an ephemeral filesystem (e.g. Render's free tier), stored data does not persist across restarts/redeploys — this is a known limitation suitable for demos and development, not production use with real user data.

Author

Built by fulfillmenta
Feel free to check more of my work on https://github.com/fulfillmenta