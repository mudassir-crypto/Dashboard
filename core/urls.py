from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('user-profile/', views.userProfile, name='user-profile'),

    path('course-form/', views.createCourse, name='course-form'),
    path('edit-course/<str:pk>', views.editCourse, name='edit-course'),
    path('delete-course/<str:pk>', views.deleteCourse, name='delete-course'),

    path('add-teacher/', views.createTeacher, name='add-teacher'),
    path('edit-teacher/<str:pk>', views.editTeacher, name='edit-teacher'),
    path('delete-teacher/<str:pk>', views.deleteTeacher, name='delete-teacher'),

    path('add-student/', views.createStudent, name='add-student'),
    path('edit-student/<str:pk>', views.editStudent, name='edit-student'),
    path('delete-student/<str:pk>', views.deleteStudent, name='delete-student'),

]