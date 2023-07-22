from django.contrib.auth.models import User
from django.db import models
from main.models import Teacher

# Create your models here.
from django.utils import timezone


class Course(models.Model):
    name=models.CharField(max_length=255)
    duration=models.CharField(max_length=255)
    # thumbnail = models.ImageField(upload_to='course_images/',default=None)
    course_image=models.ImageField(upload_to='course_images/')
    fee=models.FloatField()
    paid=models.BooleanField(default=False)
    decsription=models.TextField()
    date=models.DateField(default=timezone.now)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Topic(models.Model):
    topic=models.CharField(max_length=300)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

class Activity(models.Model):

    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    activity_name=models.CharField(max_length=255)
    video=models.FileField(upload_to='video_activity/%y')

    def __str__(self):
        return self.activity_name

class Question(models.Model):
    question=models.TextField()
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class CourseEnroll(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
