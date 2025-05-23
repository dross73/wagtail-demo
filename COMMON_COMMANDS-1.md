# 🐍 Wagtail Project – Common Commands

## 🔁 Virtual Environment
```bash
venv\Scripts\activate        # Activate virtual environment (Windows)
deactivate                     # Exit virtual environment
```

## 🛠️ Project Setup
```bash
pip install -r requirements.txt   # Install dependencies
python manage.py migrate          # Apply DB schema
python manage.py createsuperuser  # Create admin login
```

## 🚀 Development
```bash
python manage.py runserver        # Start the dev server
```

## 🧱 Page Model Changes
```bash
python manage.py makemigrations   # Detect model changes
python manage.py migrate          # Apply model changes to DB
```

## 🧼 Cleanup & Tips
```bash
Ctrl + C                          # Stop the server
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned  # Allow venv activation
```

---

Edit this list as needed! Keep it in your project root as a quick reference.
