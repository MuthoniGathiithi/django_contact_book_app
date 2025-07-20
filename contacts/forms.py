from django import forms
from .models import Contact
class ModelForm():

    class Meta:
        model = Contact
        fields = ['name', 'number', 'email']