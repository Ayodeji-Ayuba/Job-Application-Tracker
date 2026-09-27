# Job Application Tracker API

A RESTful API for tracking job applications, built with FastAPI and PostgreSQL. Users can register, log in, and manage their job applications securely with JWT authentication.

---

## Tech Stack

- **Python 3.14**
- **FastAPI** — web framework
- **PostgreSQL 18** — database
- **SQLAlchemy** — ORM
- **Pydantic v2** — data validation
- **JWT (python-jose)** — authentication
- **bcrypt / passlib** — password hashing
- **pytest** — testing

---

## Features

- User registration and login with JWT authentication
- Full CRUD for job applications
- Protected routes — users can only access their own data
- Automated test suite with 7 passing tests

---

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------------|--------------------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive a JWT token |

### Jobs
| Method | Endpoint | Description |
|--------|----------------------|-------------------------------|
| POST | `/jobs/` | Create a job application |
| GET | `/jobs/` | Get all your job applications |
| GET | `/jobs/{id}` | Get a single job application |
| PUT | `/jobs/{id}` | Update a job application |
| DELETE | `/jobs/{id}` | Delete a job application |

---

## Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/Ayodeji-Ayuba/Job-Application-Tracker.git
cd Job-Application-Tracker
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy `.env.example` to `.env` and fill in your values:
```bash
cp .env.example .env
```

```env
DATABASE_URL=postgresql://user:password@localhost:5432/job_tracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Interactive docs available at `http://127.0.0.1:8000/docs`

---

## Running Tests

### 1. Create a test environment file
```bash
cp .env.example .env.test
```

Fill in `.env.test` with your test database URL:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/job_tracker_test
```

### 2. Run the test suite
```bash
pytest tests/ -v
```

Expected output: **7 passed**

---

## Project Structure

```
Job-Application-Tracker/
├── main.py               # App entry point
├── models/
│   └── models.py         # Database models (User, JobApplication)
├── schemas/
│   └── schemas.py        # Pydantic schemas
├── routers/
│   ├── auth.py           # Auth endpoints
│   └── jobs.py           # Jobs endpoints
├── utils/
│   └── auth.py           # JWT, password hashing, dependencies
├── tests/
│   ├── conftest.py       # Test fixtures
│   ├── test_auth.py      # Auth tests
│   └── test_jobs.py      # Jobs tests
├── .env.example          # Environment variable template
└── requirements.txt
```

---

## Author

**Ayodeji** — [GitHub](https://github.com/Ayodeji-Ayuba)
**#AyodeejiOut**
