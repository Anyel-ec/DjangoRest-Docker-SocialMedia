from django.db import models

class Post(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    num_likes = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id.id,
            'title': self.title,
            'content': self.content,
            'category_id': self.category_id.id,
            'num_likes': self.num_likes,
            'num_comments': self.num_comments,
            'time_created': self.time_created
        }
