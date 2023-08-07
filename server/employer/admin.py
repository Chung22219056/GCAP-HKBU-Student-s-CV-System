from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.CompanyInformation)
admin.site.register(models.JobType)
admin.site.register(models.Job)
