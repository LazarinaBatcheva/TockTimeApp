# TockTimeApp

TockTimeApp is a Django-based web application designed to manage personal and team tasks, as well as provide a social platform for sending friend requests and managing teams. The project utilizes Django REST Framework for API endpoints, combined with a modern front-end using JavaScript for dynamic interactions.

# Installation

- Requirements
- Python 3.10+
- Django 4.2+
- PostgreSQL
- Node.js (optional, for managing front-end dependencies)

# Steps to Run Locally

1. Clone the repository:
git clone [https://github.com/yourusername/TockTimeApp.git](https://github.com/LazarinaBatcheva/TockTimeApp.git)
cd TockTimeApp

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

4. Configure the .env file with the required settings:
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://username:password@localhost:5432/tocktime

5. Apply migrations:
python manage.py migrate

6. Create a superuser:
python manage.py createsuperuser

7. Run the development server:
python manage.py runserver

8. Access the application at http://127.0.0.1:8000/
