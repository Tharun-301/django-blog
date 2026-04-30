# 🚀 Django Blogging Platform (Production-Ready + DRF API)

A full-stack blogging system built with Django, designed using real-world architecture patterns.  
This project goes beyond basic CRUD by implementing role-based access, scalable structure, and API support using Django REST Framework.

---

Live : https://Tharun381.pythonanywhere.com

----


## 🔥 Key Highlights

- Multi-role system (Admin / Manager / Editor / Author)
- Clean, scalable project structure
- Fully functional REST API (DRF)
- PostgreSQL-ready (SQLite used for development)
- Production-oriented features (media, permissions, deployment)

---

## 🧠 Why This Project Matters

Most Django projects stop at CRUD. This one doesn’t.

### What makes this different:

- Implements real authorization logic (not just login/logout)
- Uses modular app structure (not a single messy app)
- Supports both server-rendered views + API layer
- Designed for scalability and deployment

---

## 🏗️ Tech Stack

- **Backend:** Django 4.x  
- **API:** Django REST Framework  
- **Database:** SQLite (dev), PostgreSQL (production-ready)  
- **Authentication:** Django Auth + Groups + Permissions  
- **Frontend:** Django Templates (SSR)  
- **Deployment:** PythonAnywhere  

---

## ⚙️ Core Features

### 🔐 Authentication & Authorization

- Login / Logout system  
- Role-based access using Groups  
- Permission decorators for route protection  

**Example 1:**  
Editor can create/edit posts but cannot delete users  

**Example 2:**  
Manager dashboard shows analytics but restricts content editing  

---

### 📝 Blog System

- Create, edit, delete blog posts  
- Category-based filtering  
- SEO-friendly slug generation  

**Example 1:**  
`/post/django-best-practices/`  

**Example 2:**  
Auto-generated slug from title with uniqueness handling  

---

### 💬 Comment System

- Only authenticated users can comment  
- Linked to user and post  

**Example 1:**  
Anonymous users are blocked  

**Example 2:**  
Comment is tied to `request.user`  

---

### 🖼️ Media Handling

- Image uploads via `ImageField`  
- Configured `MEDIA_URL` & `MEDIA_ROOT`  

**Example 1:**  
Blog thumbnails  

**Example 2:**  
User-uploaded images stored in structured directories  

---

## 🌐 REST API (DRF)

### Endpoints
### Features

- JSON responses  
- Serializer-based validation  

**Example 1:**  
GET all posts → `/api/posts/`  

**Example 2:**  
POST new comment → `/api/comments/`  

---

## 🛠️ Setup Instructions

1. Clone Repository

```bash
git clone : git clone https://github.com/tharun-301/django-blog.git
cd BLOG

2. Create Virtual Environment
python -m venv env

## 🚀 Deployment (PythonAnywhere)

This project is deployed using PythonAnywhere, a beginner-friendly platform for hosting Django applications.
 .\env\Scripts\activate.ps1

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Create Superuser
python manage.py createsuperuser

6. Run Server
python manage.py runserver


