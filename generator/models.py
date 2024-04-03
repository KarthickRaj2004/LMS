from django.db import models

# Create your models here.
class IncompleteGeneration(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=100)
    duration=models.CharField(max_length=30)
    email=models.EmailField()
    def _str_(self):
        return self.name+' '+self.course+' '+self.duration+' '+self.email