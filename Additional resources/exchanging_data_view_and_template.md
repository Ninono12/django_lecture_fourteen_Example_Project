# 🔄 Exchanging Data Between Views and Templates in Django (FBVs)

When using **FBVs**, the primary mechanism to send data to a template is by passing a **context dictionary** to the `render()` function.

---

### 🧠 Basic Syntax

```python
from django.shortcuts import render

def my_view(request):
    context = {'key': 'value'}
    return render(request, 'template_name.html', context)
```

---

## ✅ Real Examples from CRUD Views

### 1. **Sending a List of Objects (List View)**

```python
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
```

**Template usage:**

```html
{% for book in books %}
  <p>{{ book.title }} by {{ book.author }}</p>
{% endfor %}
```

---

### 2. **Sending a Single Object (Detail View)**

```python
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
```

**Template usage:**

```html
<h1>{{ book.title }}</h1>
<p>Written by {{ book.author }} on {{ book.published_date }}</p>
```

---

### 3. **Sending a Form (Create/Update View)**

```python
def book_create(request):
    form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
```

**Template usage:**

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

---

### 4. **Sending Multiple Variables**

```python
def my_custom_view(request):
    name = "Django"
    count = 3
    items = ['A', 'B', 'C']
    return render(request, 'my_template.html', {
        'name': name,
        'count': count,
        'items': items,
    })
```

**Template usage:**

```html
<p>Hello, {{ name }}!</p>
<p>You have {{ count }} items:</p>
<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

---

### 💡 Extra Tips

* **Template Filters:** You can format data using filters, e.g. `{{ date_value|date:"F d, Y" }}`
* **Conditionals in Templates:**

```html
{% if books %}
  {% for book in books %}
    <p>{{ book.title }}</p>
  {% endfor %}
{% else %}
  <p>No books found.</p>
{% endif %}
```

* **Accessing Form Errors:**

```html
{% if form.errors %}
  <ul>
    {% for field, errors in form.errors.items %}
      <li>{{ field }}: {{ errors|join:", " }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

---
