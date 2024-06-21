from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    birthdate = models.DateField()
    salt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def to_dict(self, include_sensitive=False):
        user_dict = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'birthdate': self.birthdate
        }
        if include_sensitive:
            user_dict['password'] = self.password
            user_dict['salt'] = self.salt
        
        return user_dict
   