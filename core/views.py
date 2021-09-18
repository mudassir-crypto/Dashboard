from .forms import CourseForm, CustomUserCreationForm, ProfileForm, StudentForm, TeacherForm
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    courses_count = Course.objects.all().count()
    teachers = Teacher.objects.all()
    teachers_count = teachers.count()
    students_count = Student.objects.all().count()

    context = {'teachers': teachers, 'courses_count': courses_count, 'teachers_count': teachers_count, 'students_count': students_count}
    return render(request, 'core/dashboard.html', context)

@login_required(login_url='login')
def courses(request):
    courses = Course.objects.all()

    context = {'courses': courses}
    return render(request, 'core/courses.html', context)

@login_required(login_url='login')
def teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'core/teachers.html', context)

@login_required(login_url='login')
def students(request):
    students = Student.objects.all()
    context = {'students': students}

    return render(request, 'core/students.html', context)
    
@login_required(login_url='login')
def userProfile(request):
    form = ProfileForm()
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'core/user.html', context)

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            try:
                if form.is_valid:
                    form.save()
                    messages.success(request, "User account is created")
                    return redirect('login')  
                else:
                    messages.error(request, "An error has occured during registration")
            except:
                messages.error(request, "An error has occured during registration process")

    context = {"form": form}
    return render(request, 'core/signup.html', context)
    

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR Password is incorrect")

    return render(request, 'core/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, "User is successfully logged out!")
    return redirect('login')

@login_required(login_url='login')
def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/course_form.html', context)

@login_required(login_url='login')
def editCourse(request, pk):
    course = Course.objects.get(id=pk)

    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/course_form.html', context)

@login_required(login_url='login')
def deleteCourse(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('courses')

@login_required(login_url='login')
def createTeacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/teacher_form.html', context)

@login_required(login_url='login')
def editTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)

    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/teacher_form.html', context)

@login_required(login_url='login')
def deleteTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    return redirect('teachers')

@login_required(login_url='login')
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/teacher_form.html', context)

@login_required(login_url='login')
def editStudent(request, pk):
    student = Student.objects.get(id=pk)

    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/teacher_form.html', context)

@login_required(login_url='login')
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('students')