from django.db import models

# Create your models here.
class CV(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)


class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class Skill(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)


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