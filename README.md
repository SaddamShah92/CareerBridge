# 🧳 Django Job Board

A full-featured **Job Board web application** built with Django, allowing companies to post jobs and candidates to apply with their resumes. Role-based access ensures that HR and general users have different permissions and dashboards.

---

## 📌 Features

### 👤 Authentication & Roles
- Custom user model with two roles: `user` and `hr`
- Registration, login, and logout functionality
- Role-based dashboards and permissions

### 💼 Jobs (For HR)
- HR can:
  - Create, edit, and delete job posts
  - View applicants for each job

### 📄 Applications (For Users)
- Users can:
  - View job listings
  - Apply to jobs with a resume upload
  - Track their own applications

### 🧠 User Experience
- Bootstrap-based responsive UI
- Flash messages for all major actions (e.g., applied, posted)
- Role-specific menus and access control

---

## 🗂️ Project Structure

project_root/ │ ├── accounts/ # User management (login/register, roles) │ ├── models.py # CustomUser model with role │ ├── views.py # Auth & dashboard views │ ├── urls.py │ └── templates/accounts/ │ ├── jobs/ # Job and Application handling │ ├── models.py # Job and Application models │ ├── views.py # Job CRUD and application logic │ ├── urls.py │ └── templates/jobs/ │ ├── templates/ # Global templates (base.html, home.html) │ ├── static/ # Static files (CSS, JS, images) ├── media/ # Uploaded resumes ├── db.sqlite3 # Default DB (can use PostgreSQL) ├── manage.py └── README.md # This file


---

## 🏁 Getting Started

### 🔧 Requirements

- Python 3.8+
- Django 4.x
- Virtualenv (recommended)

### ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/django-job-board.git
cd django-job-board

# 2. Create and activate a virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
🛠️ Configuration
settings.py:
python
Copy
Edit
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static']
urls.py (project-level):
python
Copy
Edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', include('jobs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
🧪 Roles and Permissions
Role	Permissions
user	View jobs, apply, see their applications
hr	Post/edit/delete jobs, view applicants
superuser	Full admin access

📷 Screenshots

