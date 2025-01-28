from django.contrib import admin

from news.models import Course, Student, MyUser

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'is_staff')
    list_display_links = ('username',)
    list_filter = ('id', 'username', 'phone')
    search_fields = ('id', 'username', 'phone')

admin.site.register(MyUser, MyUserAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name', 'updated_at')
    search_fields = ('id', 'name')

admin.site.register(Course, CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'enrolled_at', 'course')
    list_display_links = ('name', 'email')
    list_filter = ('id', 'name', 'course')
    search_fields = ('id', 'name', 'course')

admin.site.register(Student, StudentAdmin)
