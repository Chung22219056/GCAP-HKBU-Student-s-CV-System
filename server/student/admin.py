from django.contrib import admin

from . import models
# Register your models here.
# admin.site.register(models.Account)

# admin.site.register(models.CVLanguage)
# admin.site.register(models.CVSkill)

# admin.site.register(models.Skill)


admin.site.register(models.Student)
admin.site.register(models.CvInfoBase)
# admin.site.register(models.Cv)
admin.site.register(models.Education)
admin.site.register(models.Language)
admin.site.register(models.WorkExperience)
