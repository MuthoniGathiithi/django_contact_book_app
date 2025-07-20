from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=10)
    number=models.CharField(max_length=10)
    email=models.EmailField()


# Create your models here.
