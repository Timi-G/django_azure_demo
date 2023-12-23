from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User,Student, HOD, Company, Job, JobApplication

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(HOD)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobApplication)
