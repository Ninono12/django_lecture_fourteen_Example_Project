# 🗑️ Example: Delete a Book with Confirmation

Deleting a record safely should involve:

1. A **GET** request to show a confirmation page.
2. A **POST** request to actually delete the object.

---

### 1. **Delete View (with Confirmation)**

```python
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect after deletion

    return render(request, 'books/book_confirm_delete.html', {'book': book})
```

---

### 2. **Delete Confirmation Template: `book_confirm_delete.html`**

```html
<h1>Delete Book</h1>
<p>Are you sure you want to delete <strong>{{ book.title }}</strong>?</p>

<form method="post">
  {% csrf_token %}
  <button type="submit">Yes, delete</button>
  <a href="{% url 'book_detail' book.pk %}">Cancel</a>
</form>
```

---

### 3. **URL Pattern for Delete View**

```python
# urls.py
path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
```

---

### 🧠 Flow Summary

| Step            | Action                                 |
| --------------- | -------------------------------------- |
| GET request     | Show confirmation page with book title |
| POST request    | Delete the object and redirect to list |
| `book.delete()` | Deletes the object from the database   |

---

### ✅ Optional: Add a Delete Link in List or Detail Template

```html
<a href="{% url 'book_delete' book.pk %}">Delete</a>
```
