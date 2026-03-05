from django.db import models

# --- ЗАДАНИЕ 1: УНИВЕРСИТЕТ ---

class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    semester_list = [('Spring', 'Spring'), ('Fall', 'Fall')]
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=10, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    credits = models.IntegerField()
    semester = models.CharField(max_length=10, choices=semester_list)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_year = models.IntegerField()
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course')

# --- ЗАДАНИЕ 2: БИБЛИОТЕКА (КНИГИ) ---

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title