from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return self.title
