# models.py

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to='covers/', default='default_cover.jpg')
    main_course = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_courses', null=True, blank=True)

class LearningModule(models.Model):
    title = models.CharField(max_length=100)
    sub_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='learning_modules')
    content = models.FileField(upload_to='learning_modules/')

class PowerPointPresentation(models.Model):
    title = models.CharField(max_length=100)
    sub_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='powerpoint_presentations')
    file = models.FileField(upload_to='powerpoint_presentations/')
    
    def __str__(self):
        return self.title
