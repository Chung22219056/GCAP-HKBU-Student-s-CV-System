from django.db import models

# Create your models here.

# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     location = models.CharField(max_length=255)

# class Location(models.Model):
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)

# class Category(models.Model):
#     name = models.CharField(max_length=255)

# class Job(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Category)
#     salary = models.DecimalField(max_digits=12, decimal_places=2)
#     date_posted = models.DateField()