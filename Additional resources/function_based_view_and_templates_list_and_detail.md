## 📋 List View: Display All Books

### 1. **View: `book_list`**

```python
# views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
```

---

### 2. **Template: `book_list.html`**

```html
<h1>Book List</h1>

<ul>
  {% for book in books %}
    <li>
      <a href="{% url 'book_detail' book.pk %}">{{ book.title }}</a>
    </li>
  {% empty %}
    <li>No books available.</li>
  {% endfor %}
</ul>

<a href="{% url 'book_create' %}">Add New Book</a>
```

---

### 3. **URL:**

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
]
```

---

## 📖 Detail View: Show One Book's Info

### 1. **View: `book_detail`**

```python
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
```

---

### 2. **Template: `book_detail.html`**

```html
<h1>{{ book.title }}</h1>

<p><strong>Author:</strong> {{ book.author }}</p>
<p><strong>Published Date:</strong> {{ book.published_date }}</p>

<a href="{% url 'book_update' book.pk %}">Edit</a> |
<a href="{% url 'book_delete' book.pk %}">Delete</a> |
<a href="{% url 'book_list' %}">Back to List</a>
```

---

### 3. **URL:**

```python
# urls.py
urlpatterns += [
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
```

---
