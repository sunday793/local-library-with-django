# 📚 Local Library

A web application for managing a local library catalog. Built on the Mozilla MDN tutorial, enhanced with custom improvements.


## 🎯 Features

- ✅ View book list with pagination
- ✅ Search books by title (Django ORM, `icontains`)
- ✅ Book detail page (author, genre, available copies)
- ✅ Author list and author detail pages
- ✅ Authentication and user permissions
- ✅ Admin panel for managing books, authors, and copies
- ✅ Custom CSS styling


## 🛠️ Tech Stack

- **Python 3.x**
- **Django**
- **SQLite**
- **HTML, CSS**
- **Django ORM**


## 🏗️ Project Structure
```
locallibrary/
├── catalog/ # Main application
│ ├── models.py # Models: Book, Author, BookInstance, Genre
│ ├── views.py # Views (CBV)
│ ├── urls.py # URL routes
│ ├── admin.py # Admin panel
│ └── templates/ # Templates
├── locallibrary/ # Project settings
│ ├── settings.py
│ └── urls.py
├── static/ # CSS, images
├── manage.py
└── requirements.txt
```


## 🚀 Installation and Setup

### Requirements

- Python 3.9+
- Django


### Local Setup

```bash
git clone https://github.com/sunday793/local-library-with-django.git
cd local-library-with-django
pip install -r requirements.txt
cd locallibrary
python manage.py migrate
python manage.py runserver
```


### Create Superuser (for admin panel)

```bash
python manage.py createsuperuser
```


## 🧪 Tests

```bash
python manage.py test
```


## 📝 Implementation Highlights

- **Search by title** — implemented via `get_queryset()` using `icontains`
- **Pagination** — 10 books per page via `paginate_by`
- **Class-Based Views** — `ListView` and `DetailView` for data display
- **Tests** — 5 tests covering search and view rendering


## 👩‍💻 Author
Sofia Sineglazova


## 📚 Credits

Built following the [Mozilla MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)