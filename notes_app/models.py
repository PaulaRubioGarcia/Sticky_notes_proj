# notes_app/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):  # Table name will be sticky_notes_app_note
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='notes')
