from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)
    msg = models.TextField()

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    number = models.IntegerField()

    def __int__(self):
        return self.number

class Teacher(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='teacher')
    # facebook = models.CharField(max_length=255)
    # twitter= models.CharField(max_length=300)
    # linkedin= models.CharField(max_length=300)
    designation=models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)