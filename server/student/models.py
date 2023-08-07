from django.db import models
from django.contrib.auth.models import User
import random, datetime
from django_base64field.fields import Base64Field

# Create your models here.


class Student(models.Model):
    
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profileIcon = Base64Field(max_length=900000)
    nickName = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    aboutMe = models.TextField(max_length=1000, blank=True)
    student_id = models.CharField(max_length=8, primary_key=True) # 8 digital numbers example 22221111 
    # is_first_login = models.BooleanField(default=True)
    status = models.BooleanField()

    
    def toDict(self):
        return {
            'student_id': self.student_id,
            'student_name': self.user_id.username,
            'email': self.user_id.email
        }
    
    def getName(self):
        return self.user_id.username


# class Cv(models.Model):
#      studentID =models.ForeignKey(Student, on_delete=models.CASCADE)
#      cvId = models.CharField(max_length=255, default="{0}-CV".format(random.randint(11111,99999)))
#      cvName= models.CharField(max_length=255)
#      def __str__(self):
#         return "Cv Name:[{0}]".format(self.cvName)
     
class CvInfoBase(models.Model):
    studentID =models.ForeignKey(Student, on_delete=models.CASCADE)
    cvName= models.CharField(max_length=255)
    profileIcon = Base64Field(max_length=900000,blank=True,null=True)
    cvId = models.CharField(max_length=255, default="{0}-CV".format(random.randint(11111,99999)))
    fristName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nickName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    aboutMe = models.TextField(max_length=1000, default="")
    # website = models.URLField(blank=True, null=True)
    # github = models.URLField(blank=True, null=True)

    def __str__(self):
        return "{0} student Name:[{1} {2}]".format(self.cvId,self.fristName,self.lastName)
    
    @property
    def getLanguage(self):
        return Language.objects.filter(cv=self,studentID=self.studentID)
    
    def copyInformationFromStudent(self):
        pass

class Education(models.Model):
    cv = models.ForeignKey(CvInfoBase, on_delete=models.CASCADE)
    studentID =models.ForeignKey(Student, on_delete=models.CASCADE)
    shcoolName = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.shcoolName
    
    def to_dict(self):
        return {
            'studentID': self.studentID.student_id,
            'schoolName': self.shcoolName,
            'major': self.major,
            'start_date': self.start_date.strftime("%Y-%m-%d"),
            'end_date': self.end_date.strftime("%Y-%m-%d")
        }

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
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField()

    def __str__(self):
        return "{0} {1}".format(self.studentID.user_id,self.companyName)
    
    def to_dict(self):
        return {
            'companyName': self.companyName,
            'description': self.description,
            'start_date': self.start_date.strftime("%Y-%m-%d"),
            'end_date': self.end_date.strftime("%Y-%m-%d")
        }

