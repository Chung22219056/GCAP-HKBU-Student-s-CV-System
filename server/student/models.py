from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length = 254)
    pwd = models.CharField(max_length=20)
    status = models.CharField(max_length=1)


    
class CV(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class EducationType(models.Model):
    type = models.CharField(max_length=255)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)


class Skill(models.Model):
    cv = models.ManyToManyField(CV)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Language(models.Model):
    cv = models.ManyToManyField(CV)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    employer = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class CVSkill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class CVLanguage(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)