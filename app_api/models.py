from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name