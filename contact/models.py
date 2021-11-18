from django.db import models

# Create your models here.

class Contact(models.Model):
    
    message = models.TextField(max_length=1000, null=False, blank=False)
    subject = models.TextField(max_length=1000, null=False, blank=False)
    email = models.EmailField()


    
        