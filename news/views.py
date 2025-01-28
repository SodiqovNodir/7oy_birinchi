from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.core.paginator import Paginator

from news.forms import CourseForm, StudentForm, RegisterForm, LoginForm, EmailForm
from news.models import Course, Student, MyUser


def asosiy(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 2)

    page = request.GET.get('page', 1)

    contexts = {
        'courses':paginator.page(page),
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
            courrse = course.save()
            messages.success(request, "Course muvofaqyatli o'rnatildi.")
            return redirect('tanlangan', course_id = courrse.pk)
    courses = CourseForm()
    contexts = {
        'courses' : courses,
    }
    return render(request, 'add_course.html', context = contexts)

def add_student(request: WSGIRequest):

    if request.method == 'POST':
        student = StudentForm(data=request.POST, files=request.FILES)
        if student.is_valid():
            stud = student.save()
            messages.success(request, "Student muvofaqiyatli o'rnatildi")
            return redirect('tanlangan', course_id = stud.pk)
    students = StudentForm()
    contexts = {
        'students' : students,
    }
    return render(request, 'add_student.html', context = contexts)

def update_course(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES, instance=course)
        if form.is_valid():
            course.save()
        return redirect('tanlangan', course_id = course_id)

    courses = CourseForm(instance=course)

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

def send_message_to_email(request):
    if request.method == 'POST':
        email = EmailForm(data=request.POST)
        if email.is_valid():
            subject = email.cleaned_data.get('subject')
            message = email.cleaned_data.get('message')
            users = MyUser.objects.all()
            for user in users:
                send_mail(subject,
                          message,
                          "sodiqovnodirbek14@gmail.com",
                          [user.email],
                          fail_silently=False)

            messages.success(request, 'Xabar yuborildi😍')
            return redirect('asosiy')

    else:
        email = EmailForm()
    context = {
        'email':email
    }
    return render(request, 'send_email.html', context)

