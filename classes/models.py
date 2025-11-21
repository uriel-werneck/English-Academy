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