from django.db import models
from .Province import Province
from .Gender import Gender
from .Status import Status

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    birthdate = models.DateField()
    salt = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
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
            'birthdate': self.birthdate,
            'province': self.province.to_dict() if self.province else None,
            'gender': self.gender.to_dict() if self.gender else None,
            'role': self.role.to_dict() if self.role else None,
            'status': self.status.to_dict() if self.status else None,
        }
        if include_sensitive:
            user_dict['password'] = self.password
            user_dict['salt'] = self.salt
        
        return user_dict
   