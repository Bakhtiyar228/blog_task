
```markdown
# Blog API Django

This project is a simple blog API implemented in Django, using Django REST Framework.

## Running the Project

### Requirements
- Python 3.10+

### Installation
1. Create and activate a virtual environment:
   
   ```bash
   python -m venv venv
   . venv/bin/activate  # for Unix/macOS
   venv\Scripts\activate  # for Windows
   ```

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for accessing the admin panel:
   
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   
   ```bash
   python manage.py runserver
   ```

### Accessing the Admin Panel
The admin panel is available at http://localhost:8000/admin/. Use the credentials of the superuser created earlier to log in.

### Using the API
The API provides the following endpoints:
- /api/token/: Obtain JWT token for authentication.
- /api/token/refresh/: Refresh JWT access token.
- /api/posts/: Endpoints for managing posts (GET, POST, PUT, DELETE).
- /api/comments/: Endpoints for managing comments (GET, POST, PUT, DELETE).

To access protected endpoints, include the JWT access token in the Authorization header.

### Note
For full functionality of the project, it is recommended to familiarize yourself with Django and Django REST Framework settings and documentation.

## Environment Variables
You should create a `.env` file in the root directory and fill it with your database information. Here is an example:

```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432
```
