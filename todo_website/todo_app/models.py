from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
    text = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("home")
    

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"