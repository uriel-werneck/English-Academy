from django.db import models


# Create your models here.
class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    revision_pages = models.IntegerField()
    new_work_pages = models.IntegerField()
    starts_at = models.TimeField()
    ends_at = models.TimeField()

    def __str__(self):
        return self.name
    
class ClassSheet(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    date = models.DateField()
    stage = models.IntegerField()
    initial_page = models.IntegerField()
    final_page = models.IntegerField()
    revision = models.IntegerField(blank=True, null=True)
    last_word = models.CharField(max_length=50)
    dictation = models.IntegerField(blank=True, null=True)
    lesson_check = models.IntegerField(blank=True, null=True)
    initials = models.CharField(max_length=50)
    supervisor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Class-Sheet for {self.school_class.name}"