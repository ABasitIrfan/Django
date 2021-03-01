
from django.db import models
# Create your models here.


class Project (models.Model):
    project_title = models.CharField(max_length=100)

    def __str__(self):
        return self.project_title


class student (models.Model):
    std_name = models.CharField(max_length=100)
    std_rollno = models.CharField(max_length=100)
    std_contact = models.CharField(max_length=100)
    project_title = models.ForeignKey(Project,on_delete=models.CASCADE)
