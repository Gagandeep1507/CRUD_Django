from django.db import models

# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Name