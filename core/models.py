from django.db import models
from django.contrib.auth.models import User
import uuid

class Course(models.Model):
    language = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
    )
    instructor = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True, choices=language)
    price = models.DecimalField(max_digits=7 ,decimal_places=2, null=True, blank=True)
    students = models.ManyToManyField('Student', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    salary = models.DecimalField(max_digits=7 ,decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    standard = models.CharField(max_length=200, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name