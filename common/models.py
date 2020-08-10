from django.db import models

class Post(models.Model):
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'ID: {self.id}, title: {self.title}'
