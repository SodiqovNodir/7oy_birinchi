from django.urls import path

from news.views import (asosiy, tanlangan, add_course,
                        add_student, register, login_user,
                        logout_user, update_course, send_message_to_email)

urlpatterns = [
    path('', asosiy, name = 'asosiy'),
    path('course/<int:course_id>/', tanlangan, name='tanlangan'),
    path('send-message/', send_message_to_email, name = 'send_messages'),

    path('auth/register/', register, name = 'register'),
    path('auth/login/', login_user, name = 'login_user'),
    path('auth/logout/', logout_user, name='logout'),

    path('course/add/', add_course, name = 'add_course'),
    path('lesson/add/', add_student, name = 'add_student'),
    path('course/<int:course_id>/update', update_course , name='update_course'),

]