# TockTimeApp

TockTimeApp is a Django-based web application designed to manage personal and team tasks, as well as provide a social platform for sending friend requests and managing teams. The project utilizes Django REST Framework for API endpoints, combined with a modern front-end using JavaScript for dynamic interactions.

---

## Features

### **1. User Accounts**

- Custom user model with extended profile functionality.
- User registration, login, and logout.
- Profile management (view, edit, and delete profiles).
- User search by username, first name, or last name.

### **2. Friends Management**

- Send, accept or reject friend requests.
- View a dashboard of pending friend requests.
- Remove friends from the list.
- REST API for friend-related operations.

### **3. Task Management**

#### **Personal Tasks:**

- Create, view, edit, delete, and archive personal tasks.
- Set task priorities (low, medium, high).
- Automatically handle overdue tasks.

#### **Team Tasks:**

- Create, view, edit, and delete tasks within teams.
- Assign tasks to specific team members.
- Approve or reject completed tasks.

### **4. Teams Management**

- Create, edit, view, and delete teams.
- Assign team members from friends.
- View details of the team and its tasks.

### **5. Dashboard and Notifications**

- Centralized dashboard for tasks and teams.
- Dynamic updates for friend requests using JavaScript.

---

## Installation

### **Requirements**

- Python 3.10+
- Django 4.2+
- PostgreSQL
- Node.js (optional, for managing front-end dependencies)

### **Steps to Run Locally**

1. Clone the repository:

   ```bash
   git clone [https://github.com/LazarinaBatcheva/TockTimeApp.git]
   cd TockTimeApp
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file with the required settings:

   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgres://username:password@localhost:5432/tocktime
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/`.

---

## Usage

### **API Endpoints**

The application provides REST API endpoints for managing friends. You can test these endpoints using tools like [Postman](https://www.postman.com/) or `curl`.

- **Friend Requests:**

  - List pending friend requests: `GET /friends/api/friend-requests/`
  - Send a friend request: `POST /friends/api/friend-requests/`
  - Update a friend request: `PUT /friends/api/friend-requests/<id>/`
  - Delete a friend: `DELETE /friends/api/friends-remove/<id>/`

- **Tasks:**

  - List personal tasks: `GET /tasks/<username>/personal/`
  - Create a personal task: `POST /tasks/<username>/personal/create/`
  - Manage team tasks similarly under `/team/<slug>/`.

### **Front-End**

The application uses JavaScript for dynamic interactions, including:

- Sending and managing friend requests.

---

## Project Structure

## Project Structure

```plaintext
tock_time_app/
├── static/              # CSS, JavaScript, and other static assets
├── staticfiles/         # Collected static files for deployment
├── templates/           # HTML templates for the app
├── tock_time_app/
│   ├── accounts/        # User authentication and profiles
│   ├── common/          # Shared utilities
│   ├── friends/         # Friend request and management features
│   ├── tasks/           # Personal and team tasks management
│   ├── teams/           # Team creation and management
│   ├── __init__.py      # App initialization
│   ├── asgi.py          # ASGI configuration
│   ├── settings.py      # Django project settings
│   ├── urls.py          # URL configuration
│   └── wsgi.py          # WSGI configuration
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── ...                  # Additional files and folders

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and push to your branch.
   ```bash
   git commit -m "Add your message here"
   git push origin feature/your-feature
   ```
4. Open a pull request on GitHub.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Screenshots

### **Dashboard**



### **Friend Requests**



---

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Cloudinary](https://cloudinary.com/) for media storage

