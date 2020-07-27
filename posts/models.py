from django.db import models

class Post(models.Model):
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'Message ID: {self.id}, text: {self.text}'
