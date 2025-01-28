from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)
    photo = models.ImageField(upload_to='users/photo', null=True, blank=True)

    class Meta:
        verbose_name = "Foydalanuvchi "
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['id']



class Course(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=150)
    enrolled_at = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
