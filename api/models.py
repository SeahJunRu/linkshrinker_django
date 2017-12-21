from django.db import models

# Create your models here.

# api/models.py

class URL(models.Model):
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.address
    
