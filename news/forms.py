from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from news.models import Course, Student, MyUser


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ['updated_at']

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email']
        labels = {
            'username': "Foydalanuvchi nomini kiriting",
            'email': "Elektron pochta manzilingizni kiriting",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': "form-control form-control-lg"})
        self.fields['email'].widget.attrs.update({'class': "form-control form-control-lg"})
        self.fields['password'].widget.attrs.update({'class': "form-control form-control-lg"})
        self.fields['password_repeat'].widget.attrs.update({'class': "form-control form-control-lg"})

class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        username = self.fields['username']
        password = self.fields['password']

        username.label = "Foydalanuvchi nomi kiriting"
        username.widget.attrs.update({'class': "form-control form-control-lg"})
        password.widget.attrs.update({'class': "form-control form-control-lg"})

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
        'class': "form-control"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':"form-control"
    }))