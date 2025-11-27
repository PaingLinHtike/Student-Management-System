from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
