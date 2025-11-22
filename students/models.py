from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    classes = models.ManyToManyField(
        'classes.SchoolClass',
        through='ClassEnrollment',
        related_name='students'
    )

    def __str__(self):
        return self.name

class ClassEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_class = models.ForeignKey('classes.SchoolClass', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'school_class')
    
    def __str__(self):
        return f'{self.student.name} -> {self.school_class.name}'