from django.db import models


class Contact(models.Model):
    ''' contact model and fields'''
    subject = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.subject


    
        