from django.db import models

class Status(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('inactive', 'Inactive'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
    
    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status
        }
