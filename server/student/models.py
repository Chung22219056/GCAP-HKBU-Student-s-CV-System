from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.


class Student(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=8, primary_key=True) # 8 digital numbers example 22221111 
    status = models.BooleanField()
    
class CvInfoBase(models.Model):
    studentID =models.ForeignKey(Student, on_delete=models.CASCADE)
    cvname = models.CharField(max_length=255, default="{0}-CV".format(random.randint(11111,99999)))
    fristName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nickName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    aboutMe = models.TextField(max_length=1000, default="")
    # website = models.URLField(blank=True, null=True)
    # github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.cvname
    

class Education(models.Model):
    cv = models.ForeignKey(CvInfoBase, on_delete=models.CASCADE)
    studentID =models.ForeignKey(Student, on_delete=models.CASCADE)
    shcoolName = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.shcoolName

class EducationType(models.Model):
    type = models.CharField(max_length=255)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)


class Skill(models.Model):
    cv = models.ManyToManyField(CvInfoBase)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Language(models.Model):
    cv = models.ManyToManyField(CvInfoBase)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{0} {1}".format(self.studentID.user_id,self.name)


class WorkExperience(models.Model):
    cv = models.ForeignKey(CvInfoBase, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

