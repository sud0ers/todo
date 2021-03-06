from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=False)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title