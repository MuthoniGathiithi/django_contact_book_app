from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact

def add_contact(request):
   if request.method ==  'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('view_contacts')
         messages.success(request, "Contact added successfully!")
   else:
         form = ContactForm()
   return render(request, 'contacts/add_contact.html', {'form': form})

def view_contacts(request):
    contacts= Contact.objects.all()
    return render(request, 'contacts/view_contacts.html', {'contacts': contacts})

def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Contact deleted successfully!")
        return redirect('view_contacts')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})

def update_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully!")
            return redirect('view_contacts')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update_contact.html', {'form': form, 'contact': contact})

         