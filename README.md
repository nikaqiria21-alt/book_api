Book API
A RESTful Book Management API built with Django REST Framework.

Features
User registration and login

Token-based authentication

Role-based permissions

Admin-only book update and deletion

Create and retrieve books

PostgreSQL database

Docker and Docker Compose

API documentation with Swagger

Automated tests

GitHub Actions CI

Technologies
Python 3.12

Django

Django REST Framework

PostgreSQL 16

Docker

Docker Compose

Swagger (drf-spectacular)

GitHub Actions

API Endpoints
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/login/	Login and receive a token
GET	/api/books/	Retrieve all books
POST	/api/books/	Create a book
GET	/api/books/<id>/	Retrieve one book
PUT	/api/books/<id>/	Update a book (Admin only)
PATCH	/api/books/<id>/	Partially update a book (Admin only)
DELETE	/api/books/<id>/	Delete a book (Admin only)
Authentication
This API uses Token Authentication.

Include your token in the request header:

Authorization: Token YOUR_TOKEN
Run with Docker
1. Clone the repository
git clone https://github.com/nikaqiria21-alt/book_api.git
cd book_api
2. Create a .env file
DB_NAME=book_database
DB_USER=postgres
DB_PASSWORD=your_password
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
3. Build and start containers
docker compose up --build -d
4. Apply migrations
docker compose exec web python manage.py migrate
5. Create an administrator
docker compose exec web python manage.py createsuperuser
API Documentation
Swagger UI:

http://localhost:8000/api/docs/

Django Admin:

http://localhost:8000/admin/

Run Tests
docker compose exec web python manage.py test books
Continuous Integration (CI)
GitHub Actions automatically runs Django checks, verifies migrations, and executes tests on every push and pull request.

License
No license specified yet.