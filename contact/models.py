from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    attachement = models.FileField(upload_to="contact/", null = True)
# Create your models here.
