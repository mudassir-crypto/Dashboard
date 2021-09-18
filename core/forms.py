from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Course, Profile, Teacher, Student
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['created', 'id']
        
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ['created', 'id']

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['created', 'id']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})