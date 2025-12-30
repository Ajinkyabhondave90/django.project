
# Django HTML & CSS Project

## 📌 What This Project Does

This project is a **basic Django web application** created to demonstrate how Django can be used to serve **HTML pages** with **CSS styling**, without using any database or SQL.

The project focuses on:

* Django project setup
* URL routing
* Rendering HTML templates
* Linking static CSS files
* Understanding Django request–response flow

---

## ✅ Work Done in This Project

### 🔹 Django Setup

* Created a Django project
* Configured `settings.py` for templates and static files
* Used Django’s built-in development server

### 🔹 URL Routing

* Defined URL paths using `urls.py`
* Connected URLs to Django views

### 🔹 Views

* Created Django views to handle HTTP requests
* Rendered HTML templates using `render()`

### 🔹 Templates (HTML)

* Created HTML files inside the `templates` folder
* Used Django template engine
* Loaded static files using `{% load static %}`

### 🔹 Static Files (CSS)

* Created one CSS file for styling
* Configured `STATIC_URL` and `STATICFILES_DIRS`
* Linked CSS file to HTML pages

## 🛠️ Technologies Used

* Python
* Django
* HTML
* CSS

---

## 📂 Project Structure

```
project_name/
│── project_name/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── app_name/
│   │── views.py
│   │── urls.py
│
│── templates/
│   │── index.html
│
│── static/
│   │── css/
│       │── style.css
│
│── manage.py
│── README.md
```

---

## ▶️ How to Run the Project

```bash
pip install django
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🎯 Purpose of This Project

* Practice Django basics
* Learn template rendering
* Understand static file handling
  

---

## 👤 Author

**Ajinkya Bhondve**
Backend Developer | Python | Django
