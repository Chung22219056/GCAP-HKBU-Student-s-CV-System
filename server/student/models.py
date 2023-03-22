from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=8, primary_key=True)
    status = models.BooleanField()
    
class CvInfoBase(models.Model):
    studentID =models.ForeignKey(Student, on_delete=models.CASCADE)
    fristName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nickName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # website = models.URLField(blank=True, null=True)
    # github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Education(models.Model):
    cv = models.ForeignKey(CvInfoBase, on_delete=models.CASCADE)
    studentID =models.ForeignKey(CvInfoBase, on_delete=models.CASCADE)
    shcoolName = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class EducationType(models.Model):
    type = models.CharField(max_length=255)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)


<<<<<<< HEAD

class Language(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
=======
class Skill(models.Model):
    cv = models.ManyToManyField(CV)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Language(models.Model):
    cv = models.ManyToManyField(CV)
>>>>>>> eb45f165e5ebd02f597812aa255f17194754887d
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    cv = models.ForeignKey(CvInfoBase, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

