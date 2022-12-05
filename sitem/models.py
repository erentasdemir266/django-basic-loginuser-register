from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)

    def __str__(self) :
        return self.title
