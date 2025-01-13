from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


from news.forms import CourseForm, StudentForm, RegisterForm, LoginForm
from news.models import Course, Student


def asosiy(request):
    courses = Course.objects.all()
    contexts = {
        'courses':courses,
    }
    return render(request, 'index.html', context = contexts)

def tanlangan(request, course_id):
    courses = Course.objects.filter(id = course_id)
    students = Student.objects.filter(course = course_id)
    contexts = {
        'courses' : courses,
        'students' : students,
    }
    return render(request, 'tanlangan.html', context = contexts)

def add_course(request: WSGIRequest):

    if request.method == 'POST':
        course = CourseForm(data=request.POST, files=request.FILES)
        if course.is_valid():
            Course.objects.create(**course.cleaned_data)
        return redirect('asosiy')
    courses = CourseForm()
    contexts = {
        'courses' : courses,
    }
    return render(request, 'add_course.html', context = contexts)

def add_student(request: WSGIRequest):

    if request.method == 'POST':
        student = StudentForm(data=request.POST, files=request.FILES)
        if student.is_valid():
            stud = Student.objects.create(**student.cleaned_data)
            course_id = stud.course_id
        return redirect('tanlangan', course_id = course_id)
    students = StudentForm()
    contexts = {
        'students' : students,
    }
    return render(request, 'add_student.html', context = contexts)

def update_course(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course.name = form.cleaned_data.get('name')
            course.description = form.cleaned_data.get('description')
            course.created_at = form.cleaned_data.get('created_at')
            course.updated_at = form.cleaned_data.get('updated_at')
            course.save()
        return redirect('tanlangan', course_id = course_id)
    courses = CourseForm(initial={
        'name': course.name,
        'description': course.description,
        'created': course.created_at,
        'updated': course.updated_at,
    })

    contexts = {
        'courses': courses,
    }
    return render(request, 'add_course.html', context=contexts)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password_repeat == password:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, 'Akount yaratildi 😍🥰')
                return redirect('login_user')
    context = {
            'form': RegisterForm()
    }
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            messages.success(request, 'Xush kelibsiz😍☺️')
            login(request, user)
            return redirect('asosiy')
    context = {
        'form':LoginForm(),
    }
    return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

