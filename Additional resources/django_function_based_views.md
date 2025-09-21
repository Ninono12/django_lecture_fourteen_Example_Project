# 📘 Django Function-Based Views (FBVs) – Full CRUD Examples

Let’s assume we have a simple model called `Book`:

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

---

### ✅ 1. List View – Display all Books

```python
# views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
```

**Template: `books/book_list.html`**

```html
<h1>Book List</h1>
<ul>
  {% for book in books %}
    <li><a href="{% url 'book_detail' book.id %}">{{ book.title }}</a></li>
  {% endfor %}
</ul>
```

---

### 🔍 2. Detail View – Show one Book

```python
# views.py
from django.shortcuts import get_object_or_404

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
```

**Template: `books/book_detail.html`**

```html
<h1>{{ book.title }}</h1>
<p><strong>Author:</strong> {{ book.author }}</p>
<p><strong>Published:</strong> {{ book.published_date }}</p>
```

---

### 📝 3. Create View – Add a new Book

```python
# views.py
from django.shortcuts import redirect
from .forms import BookForm

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
```

**forms.py**

```python
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
```

**Template: `books/book_form.html`**

```html
<h1>Add New Book</h1>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

---

### ✏️ 4. Update View – Edit an existing Book

```python
# views.py
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})
```

*Same template and form as the Create View*

---

### 🗑️ 5. Delete View – Delete a Book

```python
# views.py
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
```

**Template: `books/book_confirm_delete.html`**

```html
<h1>Confirm Delete</h1>
<p>Are you sure you want to delete "{{ book.title }}"?</p>
<form method="post">
  {% csrf_token %}
  <button type="submit">Yes, delete</button>
  <a href="{% url 'book_detail' book.id %}">Cancel</a>
</form>
```

---

### 🗺️ URLs Configuration

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
```
