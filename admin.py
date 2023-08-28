from django.contrib import admin

# Register your models here.
from .models import job
#@admin.register(job)
class jobAdmin(admin.ModelAdmin):
    list_display= ('gender','name','Education_Qualification','age','skills')
admin.site.register(job,jobAdmin)
