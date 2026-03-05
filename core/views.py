from django.shortcuts import render, get_object_or_404
from .models import Professor, Course, Student, Enrollment, Author, Book



def course_list(request):
    courses = Course.objects.all()
    # Фильтр по семестру из URL (например, ?semester=Spring)
    semester = request.GET.get('semester')
    if semester:
        courses = courses.filter(semester=semester)
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrolled = Enrollment.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'enrolled': enrolled})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    my_courses = Enrollment.objects.filter(student=student)
    return render(request, 'student_detail.html', {'student': student, 'my_courses': my_courses})

def professor_courses(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    courses = Course.objects.filter(professor=professor)
    return render(request, 'professor_courses.html', {'professor': professor, 'courses': courses})



def book_list(request):

    books = Book.objects.select_related('author').all()
    return render(request, 'book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})