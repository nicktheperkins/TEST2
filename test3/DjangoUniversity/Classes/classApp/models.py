from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField()
    objects = models.Manager()
    def __str__(self):
        return self.title