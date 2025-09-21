# ✏️ Example: Update a Book

We'll allow the user to update the title, author, or published date of a book.

---

### 1. **View for Updating**

```python
# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import BookForm

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Get the object to update
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)  # Redirect to the detail page
    else:
        form = BookForm(instance=book)  # Pre-fill the form with existing data
    
    return render(request, 'books/book_form.html', {'form': form})
```

---

### 2. **Reusing the Same Template: `book_form.html`**

```html
<h1>{% if form.instance.pk %}Edit{% else %}Add{% endif %} Book</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">{% if form.instance.pk %}Update{% else %}Create{% endif %}</button>
</form>

{% if form.errors %}
  <ul>
    {% for field, errors in form.errors.items %}
      <li>{{ field }}: {{ errors|join:", " }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

---

### 3. **URL Configuration**

```python
# urls.py
path('book/<int:pk>/edit/', views.book_update, name='book_update'),
```

---

### 🧠 Flow Summary

| Step               | Description                                 |
| ------------------ | ------------------------------------------- |
| GET request        | Load form pre-filled with current book data |
| POST request       | Accept user-submitted data                  |
| `instance=book`    | Tells the form to update the existing book  |
| `form.save()`      | Updates the book in the database            |
| Redirect to detail | After success, redirect to the detail view  |

---
