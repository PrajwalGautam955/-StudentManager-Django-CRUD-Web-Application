# 🎓 StudentManager – Django CRUD Web Application
A simple and responsive Django-based web application to manage student records using CRUD (Create, Read, Update, Delete) operations. This project demonstrates the use of Django's MVT architecture, PostgreSQL integration, and template-based frontend design.

## 🚀 Features

- Add, view, update, and delete student records
- Responsive and clean user interface using HTML & CSS
- PostgreSQL database integration
- Django admin panel for backend management
- Reusable templates with `base.html` layout

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3 , JS
- **Database:** PostgreSQL

## 📁 Project Structure

```
StudentManager/
├── CRUD/                # Project settings
├── myapp/               # Main app with models, views, forms
├── templates/
│   └── myapp/           # HTML templates
├── static/
│   └── css/             # Custom styles
└── manage.py
```

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/7914a4e7-5b7d-4af5-949e-f53509488215)
![image](https://github.com/user-attachments/assets/da31410d-f508-43c0-a555-21d77cb9f4e8)
![image](https://github.com/user-attachments/assets/a9403010-864f-483c-9f90-26298adcb4c2)
![image](https://github.com/user-attachments/assets/b2f62871-2cb6-45ca-a09c-727d79e4e787)
![image](https://github.com/user-attachments/assets/30c18ce9-1e15-4f99-a962-845685a46f42)

## 📝 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StudentManager.git
   cd StudentManager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL in `settings.py`

5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

8. Visit: `http://127.0.0.1:8000/`

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.



