from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=150)
    enrolled_at = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
