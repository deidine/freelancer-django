from django.contrib import admin
from .models import   Experience_user
# Register your models here.

 
class ExperienceUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience_user', 'experince_title', 'experince_description')

 
admin.site.register(Experience_user, ExperienceUserAdmin) 
