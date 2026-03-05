from django.contrib import admin
from .models import Professor, Course, Student, Enrollment, Author, Book

# Просто регистрируем всё по списку
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Author)
admin.site.register(Book)