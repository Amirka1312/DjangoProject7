from django.contrib import admin
from django.urls import path  # ВОТ ЭТОЙ СТРОЧКИ У ТЕБЯ НЕ ХВАТАЕТ
from core import views      # И эта нужна, чтобы работали твои страницы

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('professors/<int:professor_id>/courses/', views.professor_courses, name='professor_courses'),
    # Ссылки для второго задания:
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
]