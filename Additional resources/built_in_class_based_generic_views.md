# 📚 Django Class-Based Generic Views (CBVs)

Django provides built-in generic views to handle common CRUD operations quickly and with minimal code.

---

## 📦 1. ListView

### ✅ View

```python
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
```

### 🌐 URL

```python
path('books/', BookListView.as_view(), name='book_list'),
```

### 📄 Template: `book_list.html`

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

<a href="{% url 'book_create' %}">Add Book</a>
```

---

## 🔍 2. DetailView

### ✅ View

```python
from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
```

### 🌐 URL

```python
path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
```

### 📄 Template: `book_detail.html`

```html
<h1>{{ book.title }}</h1>
<p><strong>Author:</strong> {{ book.author }}</p>
<p><strong>Published:</strong> {{ book.published_date }}</p>

<a href="{% url 'book_update' book.pk %}">Edit</a> |
<a href="{% url 'book_delete' book.pk %}">Delete</a> |
<a href="{% url 'book_list' %}">Back</a>
```

---

## ➕ 3. CreateView

### ✅ View

```python
from django.views.generic.edit import CreateView
from .models import Book

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/book_form.html'
    success_url = '/books/'  # or use reverse_lazy('book_list')
```

### 🌐 URL

```python
path('books/create/', BookCreateView.as_view(), name='book_create'),
```

### 📄 Template: `book_form.html`

```html
<h1>Create Book</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

---

## 📝 4. UpdateView

### ✅ View

```python
from django.views.generic.edit import UpdateView

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/book_form.html'
    success_url = '/books/'
```

### 🌐 URL

```python
path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
```

> ✅ Reuses the same `book_form.html` template.

---

## 🗑️ 5. DeleteView

### ✅ View

```python
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
```

### 🌐 URL

```python
path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
```

### 📄 Template: `book_confirm_delete.html`

```html
<h1>Delete Book</h1>
<p>Are you sure you want to delete "{{ book.title }}"?</p>

<form method="post">
  {% csrf_token %}
  <button type="submit">Yes, delete</button>
  <a href="{% url 'book_detail' book.pk %}">Cancel</a>
</form>
```

---

## 🧠 Summary Table

| Operation | View Class   | Template Used              | Default Context Name     |
| --------- | ------------ | -------------------------- | ------------------------ |
| List      | `ListView`   | `book_list.html`           | `object_list` or `books` |
| Detail    | `DetailView` | `book_detail.html`         | `object` or `book`       |
| Create    | `CreateView` | `book_form.html`           | `form`                   |
| Update    | `UpdateView` | `book_form.html`           | `form`                   |
| Delete    | `DeleteView` | `book_confirm_delete.html` | `object` or `book`       |

---
