# 📝 Example: Creating a Book (Form → View → Template)

### 1. **Form Definition**

```python
# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
```

---

### 2. **Function-Based View**

```python
# views.py
from django.shortcuts import render, redirect
from .forms import BookForm

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after successful POST
    else:
        form = BookForm()
    
    return render(request, 'books/book_form.html', {'form': form})
```

---

### 3. **HTML Template: `book_form.html`**

```html
<h1>Add a New Book</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Create</button>
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

### 🔁 What’s Happening?

| Action                | Code Example                                           |
| --------------------- | ------------------------------------------------------ |
| Show form             | `form = BookForm()`                                    |
| Handle POST request   | `if request.method == 'POST':`                         |
| Get POST data         | `form = BookForm(request.POST)`                        |
| Check if valid        | `if form.is_valid():`                                  |
| Save to DB            | `form.save()`                                          |
| Redirect after submit | `return redirect('book_list')`                         |
| Re-render with errors | `return render(..., {'form': form})` after failed POST |

---

### 🧪 Bonus: Receiving Individual Fields

If you're using a **manual HTML form (not `ModelForm`)**, you can retrieve specific fields like this:

```python
def custom_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        print(name, age)  # Do something with the values
    return render(request, 'my_custom_form.html')
```

**Template:**

```html
<form method="post">
  {% csrf_token %}
  <input type="text" name="name" placeholder="Your name">
  <input type="number" name="age" placeholder="Your age">
  <button type="submit">Submit</button>
</form>
```

---
