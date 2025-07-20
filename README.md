# Django Contacts App

A simple Django-based web application that allows users to add and view contacts with ease.  
This mini project is ideal for beginners learning Django and covers models, views, forms, and templates.

---

##  Features

- ✅ Add new contacts (name, phone number, email)
- ✅ View all saved contacts in a list
- ✅ Form validation with error handling
- ✅ Redirects on success
- ✅ Clean and simple interface

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django 4.x
- **Database**: SQLite (default with Django)
- **Frontend**: HTML5, CSS3 (Django templates)

---

##  Project Structure

contacts_project/
├── contacts/ # Django app
│ ├── migrations/
│ ├── templates/
│ │ └── contacts/
│ │ ├── add_contact.html
│ │ └── view_contacts.html
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py # Django form for contact
│ ├── models.py # Contact model
│ ├── tests.py
│ └── views.py # Handles add/view contact logic
├── contacts_project/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py # Project URL configuration
│ └── wsgi.py
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md



---

##  Models

**Contact Model**
```python
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
 Templates
add_contact.html – Form page
view_contacts.html – Displays list of contacts

