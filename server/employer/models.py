from django.db import models

# Create your models here.
class CompanyInformation(models.Model):
    contact_person = models.CharField(max_length=32) #Name of Contact Person
    email = models.CharField(max_length=64) #Email Address
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=128)
    website =  models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.company_name

class JobType(models.Model):
    type_name = models.CharField(max_length=32)

class Job(models.Model):
    title = models.CharField(max_length=64)
    start_date = models.DateField(null=True)
    duration = models.CharField(max_length=128)
    salary = models.IntegerField(default=0)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    job_requirement = models.CharField(max_length=512)
    job_description = models.CharField(max_length=512)
    application_method = models.CharField(max_length=512)
    remarks = models.CharField(max_length=512)
    company_id = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)

